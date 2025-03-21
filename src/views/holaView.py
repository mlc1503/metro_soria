from flet import *
from styles import *


def draw():
    view = SafeArea(
        Column(
            alignment= MainAxisAlignment.CENTER,
            controls=[
                Text("Hollaaasdsadsa"),
                Button("Volver", on_click= lambda _: Page.go("/"))
            ]
        ),
    ) 
    return view