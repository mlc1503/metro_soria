from flet import *
from styles import *

# RESOURCES:
# https://github.com/flet-dev/flet/discussions/861
def draw(page: Page):
    view = SafeArea(
        Column(
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls=[
                TextField(
                    label=Text("Origen"),
                    border_color=PRIMARY_BLUE,
                ),
                TextField(
                    label=Text("Destino"),
                    border_color=PRIMARY_BLUE,
                ),
                ElevatedButton(
                    "Buscar", 
                    on_click= lambda _: page.go("/buscar"),
                    # style=ButtonStyle(shape=RoundedRectangleBorder(10))
                )
            ]
        )
    )
    return view