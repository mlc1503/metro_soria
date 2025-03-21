from flet import *
from styles import *


def draw(page: Page):
    view = SafeArea(
        Column(
            alignment= MainAxisAlignment.CENTER,
            controls=[
                Text("Hollaaasdsadsa"),
                Button("Volver", on_click= lambda _: page.go("/"))
            ]
        ),
    ) 
    return view