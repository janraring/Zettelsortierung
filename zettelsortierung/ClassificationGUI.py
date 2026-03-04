import asyncio
from enum import Enum

from nicegui import ui, app

from zettelsortierung.DataTypes import Zettel, TopCategory


class ManualClassification:
    def __init__(self, zettels: list[Zettel], classes: Enum):
        assert len(zettels) > 0
        
        self.zettels = zettels
        self.classes = classes
        self.index = 0
        self.classifications = dict()
        self.done = asyncio.get_event_loop().create_future()

        with ui.row():
            self.back_button = ui.button('Back', on_click=lambda: self.back())
            self.stop_button = ui.button('Stop', on_click=lambda: self.abort())

        with ui.row():
            self.recto_image = ui.image(zettels[self.index].recto.full_path).props(f"width=750px height=500px")
            self.verso_image = ui.image(zettels[self.index].verso.full_path).props(f"width=750px height=500px")

        with ui.row():
            self.class_buttons = [ui.button(category.name,
                                            on_click=lambda c=category: self.next_image(c))
                                  for category in classes]
        
        self.back_button.disable()

    async def run(self):
        return await self.done

    def abort(self):
        self.done.set_result(self.classifications)
    
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

    def back(self):
        self.decrement_index()

    def next_image(self, label: str):
        self.classifications[self.zettels[self.index]] = label
        self.increment_index()



def run_classification(zettels: list[Zettel], classes: list[str]) -> dict:
    """Blocking call: opens a browser UI, returns results when the user is done."""
    results = {}

    @ui.page('/')
    async def page():
        nonlocal results
        classifier = ManualClassification(zettels, classes)

        async def wait_for_results():
            nonlocal results
            results = await classifier.run()
            # Shut down the server so ui.run() returns
            app.shutdown()

        asyncio.create_task(wait_for_results())

    ui.run(dark=None, reload=False)  # blocks until app.shutdown() is called
    return results

    
# Example standalone usage
if __name__ in {"__main__", "__mp_main__"}:
    zettels = [
        Zettel('/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/A01_a-Adel/1/01_a/00000001_1#A01_1_01_a.jpg'),
        Zettel('/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/A01_a-Adel/1/01_a/00000003_1#A01_1_01_a.jpg'),
        Zettel('/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/A01_a-Adel/1/01_a/00000005_1#A01_1_01_a.jpg'),
        Zettel('/home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/raw/zettelsammlung/A01_a-Adel/1/01_a/00000007_1#A01_1_01_a.jpg')
    ]

    #classes = ["Cat", "Dog", "Other"]

    print(run_classification(zettels, TopCategory))