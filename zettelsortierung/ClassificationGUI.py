from enum import Enum
from typing import Callable, Optional
from random import shuffle
from functools import partial

from nicegui import ui, app, run
import asyncio

from zettelsortierung.DataTypes import Zettel
from zettelsortierung.Sammlungen import Label


class ManualClassification:
    def __init__(
        self,
        classes: type[Enum],
        on_classify: Optional[Callable[[Zettel, Label], None]] = None,
        queries: Optional[dict[str, Callable[[], list[Zettel]]]] = None,
        get_stats: Optional[Callable[[], dict[str, int]]] = None,
        search_ocr_results: Optional[
            Callable[[str, Optional[bool]], list[Zettel]]
        ] = None,
        get_status: Optional[Callable[[Zettel], bool]] = None,
        get_predictions: Optional[Callable[[Zettel], list[tuple[str, float]]]] = None,
    ):

        self.queries = queries
        self.classes = classes
        self.on_classify = on_classify
        self.get_stats = get_stats
        self.search_ocr_results = search_ocr_results
        self.get_status = get_status
        self.get_predictions = get_predictions

        self.pattern = ""

        self.zettels: list[Zettel] = []
        self.index: int = 0

        # -- Top row --
        with ui.row().classes("items-center w-full"):
            self.prev_button = ui.button(
                "Prev", on_click=lambda: self.decrement_index()
            )
            self.next_button = ui.button(
                "Next", on_click=lambda: self.increment_index()
            )
            self.stop_button = ui.button("Finish", on_click=lambda: app.shutdown())
            self.shuffle_button = ui.button("Shuffle", on_click=self.shuffle_zettels)

            # -- Dropdown button for selecting a view--
            if not queries is None:
                with ui.dropdown_button("Sammlungen", auto_close=True):
                    for name, query in queries.items():
                        ui.item(
                            name,
                            on_click=lambda e, n=name, q=query: self.load_query(n, q),
                        )

            # -- Search bar --
            self.input = ui.input(label="Schlagwort").on("keydown.enter", self.on_enter)
            self.fuzzy_cb = ui.checkbox("Fuzzy", value=True)

            self.progress_bar = ui.linear_progress(value=0, show_value=False).classes(
                "w-md h-9"
            )
            self.progress_label = ui.label(f"").classes("text-base font-bold")
            ui.space()
            self.zettel_label = ui.label(f"").classes("text-base font-bold")

        # -- Images --
        with ui.row():
            self.recto_image = ui.image().props(f"width=750px height=500px")
            self.verso_image = ui.image().props(f"width=750px height=500px")

        # --Class buttons --
        with ui.row():
            self.class_buttons = [
                ui.button(
                    category.name, on_click=lambda e, c=category: self.classify_image(c)
                )
                for category in classes
            ]

        # -- Stats display --
        with ui.row().classes("items-center"):
            self.stats_label = ui.label("")

        self.prev_button.disable()
        self.next_button.disable()

        if self.get_stats:
            asyncio.create_task(self.update_stats())

        # -- Initial Zettel --
        self.set_zettels(
            [
                Zettel(
                    "/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/T11_Tref-I-Triasel/2/14_Trekkeharmonika/00726531_1#T11_2_14_Trekkeharmonika.jpg"
                )
            ]
        )

    def set_zettels(self, zettels):
        self.zettels = zettels
        self.index = 0

        self.prev_button.disable()
        self.next_button.enable()
        for b in self.class_buttons:
            b.enable()

        self.update_images()
        self.update_progress()

        self.update_predictions()

        ui.notify(f"Loaded {len(zettels)} Zettel")

    def shuffle_zettels(self) -> None:
        shuffle(self.zettels)
        self.set_zettels(self.zettels)

    async def on_enter(self, e):
        if self.search_ocr_results is None:
            return
        input = e.sender.value
        callback = partial(self.search_ocr_results, input, self.fuzzy_cb.value)
        zettels = await run.io_bound(callback)
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
        stats = self.get_stats()
        self.stats_label.set_text(f"Total: {stats.get('Total', 0)}")
        for button in self.class_buttons:
            category = button.text.split(" ")[0]  # Remove count from text
            count = stats.get(category, 0)
            button.set_text(f"{category} ({count})")

    def update_images(self):
        self.recto_image.set_source(self.zettels[self.index].recto.full_path)
        self.verso_image.set_source(self.zettels[self.index].verso.full_path)
        self.zettel_label.text = self.zettels[self.index].id

        if self.get_status is None:
            self.zettel_label.classes("bg-transparent", remove="bg-green-700")
            return
        if self.get_status(self.zettels[self.index]):
            self.zettel_label.classes("bg-green-700", remove="bg-transparent")
            return
        self.zettel_label.classes("bg-transparent", remove="bg-green-700")

    def update_progress(self):
        length = len(self.zettels)
        self.progress_bar.value = self.index / length
        self.progress_label.text = f"{self.index}/{length}"

    def confidence_to_color(self, confidence: float) -> str:
        """Map confidence [0, 1] to a red→yellow→green RGB color."""
        ui.notify(f"Confidence: {confidence:.2f}")
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
        for button in self.class_buttons:
            category = button.text.split(" ")[0]
            confidence = next(
                (conf for cat, conf in predictions if cat == category), None
            )
            if confidence is not None:
                color = self.confidence_to_color(confidence)
                button.style(f"background-color: {color} !important; color: white;")
            else:
                button.style("background-color: transparent; color: inherit;")

    async def increment_index(self):
        self.index = min(self.index + 1, len(self.zettels))
        self.update_progress()
        await self.update_stats()

        self.prev_button.enable()
        if self.index == len(self.zettels):
            ui.notify("Reached End of Collection")
            self.next_button.disable()
            for b in self.class_buttons:
                b.disable()
        else:
            self.update_images()
            self.update_predictions()

    def decrement_index(self):
        self.index = max(self.index - 1, 0)
        self.update_progress()

        self.next_button.enable()
        for b in self.class_buttons:
            b.enable()
        if self.index == 0:
            self.prev_button.disable()
        self.update_images()
        self.update_predictions()

    async def classify_image(self, selected: Enum):
        zettel = self.zettels[self.index]
        label = Label(selected, 1.0)
        if self.on_classify:
            self.on_classify(zettel, label)
        await self.increment_index()


def run_classification(
    classes: type[Enum],
    on_classify: Optional[Callable[[Zettel, Label], None]] = None,
    queries: Optional[dict[str, Callable[[], list[Zettel]]]] = None,
    get_stats: Optional[Callable[[], dict[str, int]]] = None,
    search_ocr_results: Optional[Callable[[str, Optional[bool]], list[Zettel]]] = None,
    get_status: Optional[Callable[[Zettel], bool]] = None,
    get_predictions: Optional[Callable[[Zettel], list[tuple[str, float]]]] = None,
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
