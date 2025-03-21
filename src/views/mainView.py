from flet import *
from styles import *

# RESOURCES:
# https://github.com/flet-dev/flet/discussions/861
def drawUI():
    view = SafeArea(
        Column(
                alignment= MainAxisAlignment.CENTER,
                controls=[
                    TextField(
                        label=Text("Origen", color= PRIMARY_BLUE),
                        border_color=PRIMARY_BLUE,
                    ),
                    TextField(
                        label=Text("Destino", color= PRIMARY_BLUE),
                        border_color=PRIMARY_BLUE,
                    ),
                    Button("Buscar", on_click= lambda _: Page.go("/hola"))
                ]
            ),
        ) 
    return view