import flet as ft
import styles as css


def main(page: ft.Page):
    
    page.add(
        ft.SafeArea(
            ft.Container(
                content=ft.ElevatedButton("Page theme button"),
                bgcolor=css.PRIMARY_BLUE,
                padding=20,
                width=300,
            ),
        )
    )


ft.app(main)
