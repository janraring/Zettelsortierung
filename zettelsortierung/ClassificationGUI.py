from enum import Enum
from typing import Callable, Optional

from nicegui import ui, app, run

from zettelsortierung.DataTypes import Zettel#, Classifiers, TopCategory


class ManualClassification:
    def __init__(
            self,
            queries: dict[str, Callable[[], list[Zettel]]],
            classes: type[Enum],
            on_classify: Optional[Callable[[Zettel, dict[Enum, float]], None]] = None):
        
        self.queries = queries
        self.classes = classes
        self.on_classify = on_classify

        self.zettels: list[Zettel] = []
        self.index: int = 0

        # -- Top row --
        with ui.row().classes('items-center w-full'):
            self.prev_button = ui.button('Prev', on_click=lambda: self.decrement_index())
            self.next_button = ui.button('Next', on_click=lambda: self.increment_index())
            
            # -- Dropdown button for selecting a view--
            with ui.dropdown_button('Sammlung', auto_close=True):
                for name, query in queries.items():
                    ui.item(name, on_click=lambda e, n=name, q=query: self.load_query(n, q))
                    
            self.stop_button = ui.button('Finish', on_click=lambda: app.shutdown())#self.abort())
            self.progress_bar = ui.linear_progress(value=0, show_value=False).classes('w-md h-9')
            self.progress_label = ui.label(f'').classes('text-base font-bold')
            ui.space()
            self.zettel_label = ui.label(f'').classes('text-base font-bold')

        # -- Images --
        with ui.row():
            self.recto_image = ui.image().props(f"width=750px height=500px")
            self.verso_image = ui.image().props(f"width=750px height=500px")

        # --Class buttons --
        with ui.row():
            self.class_buttons = [
                ui.button(category.name, on_click=lambda e, c=category: self.classify_image(c))
                for category in classes
            ]
        
        self.prev_button.disable()
        self.next_button.disable()
    
    async def load_query(self, name: str, query: Callable[[], list[Zettel]]):
        ui.notify(f'Loading "{name}"...')

        zettels = await run.io_bound(query)  # called fresh each time

        if not zettels:
            ui.notify(f'"{name}" returned no results')
            return

        self.zettels = zettels
        self.index = 0

        self.prev_button.disable()
        self.next_button.enable()
        for b in self.class_buttons:
            b.enable()

        self.update_images()
        self.update_progress()

        ui.notify(f'Loaded "{name}" — {len(zettels)} zettel')
    
    def update_images(self):
        self.recto_image.set_source(self.zettels[self.index].recto.full_path)
        self.verso_image.set_source(self.zettels[self.index].verso.full_path)
        self.zettel_label.text = self.zettels[self.index].id
    
    def update_progress(self):
        length = len(self.zettels)
        self.progress_bar.value = self.index/length
        self.progress_label.text = f'{self.index}/{length}'
    
    def increment_index(self):
        self.index = min(self.index + 1, len(self.zettels))
        self.update_progress()

        self.prev_button.enable()
        if self.index == len(self.zettels):
            ui.notify('Reached End of Collection')
            self.next_button.disable()
            for b in self.class_buttons: b.disable()
        else:
            self.update_images()
    
    def decrement_index(self):
        self.index = max(self.index - 1, 0)
        self.update_progress()

        self.next_button.enable()
        for b in self.class_buttons: b.enable()
        if self.index == 0:
            self.prev_button.disable()
        self.update_images()

    def classify_image(self, selected: Enum):
        zettel = self.zettels[self.index]
        probabilities = {selected: 1.0}
        if self.on_classify:
            self.on_classify(zettel, probabilities)
        self.increment_index()


def run_classification(queries: dict[str, Callable[[], list[Zettel]]],
                       classes: type[Enum],
                       on_classify: Optional[Callable[[Zettel, dict[Enum, float]], None]] = None) -> None:
    @ui.page('/')
    async def _():
        ManualClassification(queries, classes, on_classify)

    ui.run(dark=None, reload=False)