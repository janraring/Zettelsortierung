from enum import Enum
from typing import Callable, Optional

from nicegui import ui, app

from zettelsortierung.DataTypes import Zettel, TopCategory


class ManualClassification:
    def __init__(self,
                 zettels: list[Zettel],
                 classes: type[Enum],
                 on_classify: Optional[Callable[[Zettel, dict[Enum, float]], None]] = None):
        assert len(zettels) > 0
        
        self.zettels: list[Zettel] = zettels
        self.classes: type[Enum] = classes
        self.on_classify: Optional[Callable[[Zettel, dict[Enum, float]], None]] = on_classify
        self.index: int = 0

        with ui.row():
            self.back_button = ui.button('Back', on_click=lambda: self.prev_image())
            self.stop_button = ui.button('Finish', on_click=lambda: self.abort())

        with ui.row():
            self.recto_image = ui.image(zettels[self.index].recto.full_path).props(f"width=750px height=500px")
            self.verso_image = ui.image(zettels[self.index].verso.full_path).props(f"width=750px height=500px")

        with ui.row():
            self.class_buttons = [ui.button(category.name,
                                            on_click=lambda e, c=category: self.next_image(c))
                                  for category in classes]
        
        self.back_button.disable()

    def abort(self):
        print('done')
        app.shutdown()
    
    def update_images(self):
        self.recto_image.set_source(self.zettels[self.index].recto.full_path)
        self.verso_image.set_source(self.zettels[self.index].verso.full_path)
    
    def increment_index(self):
        self.index = min(self.index+1, len(self.zettels))
        self.back_button.enable()
        if self.index == len(self.zettels):
            ui.notify('Reached End of Collection')
            for b in self.class_buttons: b.disable()
        else:
            self.update_images()
    
    def decrement_index(self):
        self.index = max(self.index-1, 0)
        for b in self.class_buttons: b.enable()
        if self.index == 0:
            self.back_button.disable()
        self.update_images()

    def next_image(self, label: Enum):
        if self.on_classify:
            self.on_classify(self.zettels[self.index], {label: 1.0})
        self.increment_index()

    def prev_image(self):
        self.decrement_index()



def run_classification(zettels: list[Zettel],
                       classes: type[Enum],
                       on_classify: Optional[Callable[[Zettel, dict[Enum, float]], None]] = None) -> None:
    @ui.page('/')
    async def _():
        ManualClassification(zettels, classes, on_classify)

    ui.run(dark=None, reload=False)

    
# Example standalone usage
if __name__ in {"__main__", "__mp_main__"}:
    zettels = [
        Zettel('/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/A01_a-Adel/1/01_a/00000001_1#A01_1_01_a.jpg'),
        Zettel('/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/A01_a-Adel/1/01_a/00000003_1#A01_1_01_a.jpg'),
        Zettel('/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/A01_a-Adel/1/01_a/00000005_1#A01_1_01_a.jpg'),
        Zettel('/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/A01_a-Adel/1/01_a/00000007_1#A01_1_01_a.jpg')
    ]
    on_classify = lambda zettel, label: print(f'{zettel}: {label}')

    print(run_classification(zettels, TopCategory, on_classify))