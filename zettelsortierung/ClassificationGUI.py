from enum import Enum
from functools import partial
from random import shuffle
from typing import Callable, Optional

from nicegui import app, run, ui

from zettelsortierung.DataTypes import Classifiers, Label, Zettel


class ManualClassification:
    def __init__(
        self,
        classes: type[Enum],
        on_classify: Optional[Callable[[Zettel, Label], None]] = None,
        queries: Optional[dict[str, Callable[..., list[Zettel]]]] = None,
        get_stats: Optional[Callable[[], dict[str, int]]] = None,
        search_ocr_results: Optional[Callable[[str, Optional[bool]], list[Zettel]]] = None,
        get_status: Optional[Callable[[Zettel], bool]] = None,
        get_predictions: Optional[Callable[[Zettel], list[Label]]] = None,
    ):

        self.queries = queries
        self.sammlungen = classes
        self.on_classify = on_classify
        self.get_stats = get_stats
        self.search_ocr_results = search_ocr_results
        self.get_image_status = get_status
        self.get_predictions = get_predictions

        self.zettels: list[Zettel] = []
        self.index: int = 0
        self.selector_class = None

        # -- Top row --
        with ui.row().classes("items-center w-full"):
            self.prev_button = ui.button("Prev", on_click=lambda: self.decrement_index())
            self.next_button = ui.button("Next", on_click=lambda: self.increment_index())
            self.stop_button = ui.button("Finish", on_click=lambda: app.shutdown())
            self.shuffle_button = ui.button("Shuffle", on_click=self.shuffle_zettels)

            # -- Random sampling --
            self.select_n = ui.select([100, 1000, 10000], value=100)
            ui.button("Sample", on_click=self.sample_randomly)

            # -- Query selection --
            classifiers_names = [classifier.name for classifier in Classifiers]
            sammlungen_names = [sammlung.name for sammlung in self.sammlungen]
            self.select_classifier = ui.select(classifiers_names, value=Classifiers.MANUELL.name)
            # -- Filter for a collection --
            ui.input("Sammlung", autocomplete=sammlungen_names).on(
                "keydown.enter", lambda e: self.on_enter_filter(e)
            )

            # -- Search bar --
            self.input = ui.input(label="Klartext").on("keydown.enter", self.on_enter_search)
            self.fuzzy_cb = ui.checkbox("Fuzzy", value=False)

            # -- Progress bar --
            self.progress_bar = ui.linear_progress(value=0, show_value=False).classes("w-md h-9")
            self.progress_label = ui.label("").classes("text-base font-bold")

            # -- Total stats --
            self.total_stats_label = ui.label("")

            ui.space()

            # -- Zettel status --
            self.zettel_label = ui.label("").classes("text-base font-bold")

        with ui.grid(columns="auto auto"):
            # -- Images --
            with ui.column():
                self.recto_image = ui.image().props("width=750px height=500px")
                self.verso_image = ui.image().props("width=750px height=500px")

                with ui.row().classes("items-center w-full"):
                    # -- Class selector --
                    self.class_select = ui.select(
                        options={category: category.name for category in classes},
                        with_input=True,
                        on_change=lambda e: self.set_selector_class(e.value),
                    )
                    # -- Classify button --
                    ui.button(
                        "Classify",
                        on_click=lambda: self.classify_image(self.selector_class),
                    )

            # -- Class buttons --
            with ui.row().style("column-gap: 5px; row-gap: 0px"):
                self.class_buttons = [
                    ui.button(
                        category.name,
                        on_click=lambda e, c=category: self.classify_image(c),
                    ).style("padding: 0 5px; font-size: 16px")
                    for category in classes
                    if category.name[:4].upper() not in {"ANON", "LAUT"}
                ]

            # -- Top prediction buttons --
            if self.get_predictions:
                self.top_predictions_buttons = ui.column()

        self.prev_button.disable()
        self.next_button.disable()

        if self.get_stats:
            ui.timer(0, self.update_stats, once=True)

    def set_selector_class(self, value):
        self.selector_class = value

    def set_zettels(self, zettels):
        self.zettels = zettels
        self.index = 0

        self.prev_button.disable()
        self.next_button.enable()
        for b in self.class_buttons:
            b.enable()

        self.update_image_display()
        self.update_progress_bar()

        self.update_predictions()

        ui.notify(f"Loaded {len(zettels)} Zettel")

    def shuffle_zettels(self) -> None:
        shuffle(self.zettels)
        self.set_zettels(self.zettels)

    async def on_enter_search(self, e):
        if self.search_ocr_results is None:
            return
        input = e.sender.value
        callback = partial(self.search_ocr_results, input, self.fuzzy_cb.value)
        zettels = await run.io_bound(callback)
        self.set_zettels(zettels)

    async def on_enter_filter(self, e):
        if self.queries is None:
            return
        if self.queries.get("Filter", None) is None:
            return
        input = e.sender.value.upper()
        callback = self.queries["Filter"]
        classifier = Classifiers[self.select_classifier.value]  # type: ignore
        query = partial(callback, classifier, self.sammlungen[input])
        zettels = await run.io_bound(query)
        self.set_zettels(zettels)

    async def sample_randomly(self):
        if self.queries is None:
            return
        if self.queries.get("Random", None) is None:
            return
        callback = self.queries["Random"]
        query = partial(callback, self.select_n.value)
        zettels = await run.io_bound(query)
        self.set_zettels(zettels)

    async def on_enter_sammlung(self, e):
        if self.queries is None:
            return
        input = e.sender.value.title()
        if input not in self.queries.keys():
            ui.notify(f'There is no class named "{input}".')
            return
        zettels = await run.io_bound(self.queries[input])
        self.set_zettels(zettels)

    async def load_query(self, name: str, query: Callable[[], list[Zettel]]):
        zettels = await run.io_bound(query)
        if not zettels:
            ui.notify(f'"{name}" returned no results')
            return
        self.set_zettels(zettels)

    async def update_stats(self):
        if not self.get_stats:
            return
        stats = await run.io_bound(self.get_stats)
        self.total_stats_label.set_text(f"Total: {stats.get('Total', 0)}")
        for button in self.class_buttons:
            category = button.text.split(" ")[0]
            count = stats.get(category, 0)
            button.set_text(f"{category} ({count})")

    def update_image_display(self):
        new_zettel = self.zettels[self.index]
        self.recto_image.set_source(new_zettel.recto.full_path)
        self.verso_image.set_source(new_zettel.verso.full_path)
        self.zettel_label.text = new_zettel.id

    def update_image_status(self):
        if self.get_image_status is None:
            self.zettel_label.classes("bg-transparent", remove="bg-green-700")
            return
        if self.get_image_status(self.zettels[self.index]):
            self.zettel_label.classes("bg-green-700", remove="bg-transparent")
            return
        self.zettel_label.classes("bg-transparent", remove="bg-green-700")

    def update_progress_bar(self):
        length = len(self.zettels)
        self.progress_bar.value = self.index / length
        self.progress_label.text = f"{self.index}/{length}"

    def confidence_to_color(self, confidence: float) -> str:
        """Map confidence [0, 1] to a red→yellow→green RGB color."""
        if confidence <= 0.5:
            #  Red (150,0,0) → Yellow (150,150,0)
            t = confidence / 0.5
            r, g, b = 150, int(150 * t), 0
        else:
            #  Yellow (150,150,0) → Green (0,150,0)
            t = (confidence - 0.5) / 0.5
            r, g, b = int(150 - 150 * t), 150, 0
        return f"rgb({r},{g},{b})"

    def update_predictions(self):
        if not self.get_predictions:
            return
        predictions = self.get_predictions(self.zettels[self.index])

        self.top_predictions_buttons.clear()
        with self.top_predictions_buttons.style("column-gap: 5px; row-gap: 5px"):
            classes = [cat for cat, _ in predictions]

            with ui.row().style("column-gap: 5px; row-gap: 5px"):
                top_buttons_1 = [
                    ui.button(
                        category.name,
                        on_click=lambda e, c=category: self.classify_image(c),
                    ).style("padding: 0 5px; font-size: 16px")
                    for category in classes[:5]
                ]
            with ui.row().style("column-gap: 5px; row-gap: 5px"):
                top_buttons_2 = [
                    ui.button(
                        category.name,
                        on_click=lambda e, c=category: self.classify_image(c),
                    ).style("padding: 0 5px; font-size: 16px")
                    for category in classes[5:]
                ]

        # Colorize buttons
        for button in self.class_buttons + top_buttons_1 + top_buttons_2:
            category = button.text.split(" ")[0]
            confidence = next((conf for cat, conf in predictions if cat.name == category), None)
            if confidence is not None:
                color = self.confidence_to_color(confidence)
                button.style(f"background-color: {color} !important; color: white;")
            else:
                button.style("background-color: transparent; color: inherit;")

    def increment_index(self):
        self.index = min(self.index + 1, len(self.zettels))
        self.update_progress_bar()

        # Toggle buttons where necessary
        self.prev_button.enable()
        if self.index == len(self.zettels):
            ui.notify("Reached End of Collection")
            self.next_button.disable()
            for b in self.class_buttons:
                b.disable()

        # Update UI elements
        self.update_image_display()
        self.update_image_status()
        self.update_predictions()

    def decrement_index(self):
        self.index = max(self.index - 1, 0)
        self.update_progress_bar()

        # Toggle buttons where necessary
        self.next_button.enable()
        for b in self.class_buttons:
            b.enable()
        if self.index == 0:
            self.prev_button.disable()

        # Update UI elements
        self.update_image_display()
        self.update_image_status()
        self.update_predictions()

    async def classify_image(self, selected: Enum | None):
        if selected is None:
            return
        # Current Zettel
        zettel = self.zettels[self.index]
        # Create label
        label = Label(selected, 1.0)
        if self.on_classify:
            self.on_classify(zettel, label)
            await self.update_stats()
        self.increment_index()


def run_classification(
    classes: type[Enum],
    on_classify: Optional[Callable[[Zettel, Label], None]] = None,
    queries: Optional[dict[str, Callable[[], list[Zettel]]]] = None,
    get_stats: Optional[Callable[[], dict[str, int]]] = None,
    search_ocr_results: Optional[Callable[[str, Optional[bool]], list[Zettel]]] = None,
    get_status: Optional[Callable[[Zettel], bool]] = None,
    get_predictions: Optional[Callable[[Zettel], list[Label]]] = None,
) -> None:
    @ui.page("/")
    async def _():
        ManualClassification(
            classes,
            on_classify,
            queries,
            get_stats,
            search_ocr_results,
            get_status,
            get_predictions,
        )

    ui.run(dark=None, reload=False)
