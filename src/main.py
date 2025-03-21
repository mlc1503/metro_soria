import flet as ft
from styles import PRIMARY_BLUE, PRIMARY_CYAN, SECONDARY_CYAN, ALERT_RED, MAIN_BLACK, MAIN_WHITE, SLIGHT_BLUE

import flet as ft


def main(page: ft.Page):
    page.title = "Calc App"
    

    class TestWidget(ft.Column):
        def __init__(self, text):
            super().__init__()
            self.controls = [
                ft.Text(text, color=MAIN_WHITE)
            ]

    page.add(
        ft.SafeArea(
            ft.Container(
                bgcolor=ft.colors.BLACK,
                border_radius=ft.border_radius.all(20),
                padding=20,
                content=ft.Column(
                    controls=[
                        TestWidget("hola12")
                    ]
                ),
            ),
        ),
    )


ft.app(target=main)