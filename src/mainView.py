import flet as ft
from styles import PRIMARY_BLUE, PRIMARY_CYAN, SECONDARY_CYAN, ALERT_RED, MAIN_BLACK, MAIN_WHITE, SLIGHT_BLUE

class MainView:
    def __init__(self) ->None: pass
        # ft.Column(
        #     horizontal_alignment= ft.MainAxisAlignment.CENTER,
        #     controls=[
        #         ft.TextField(
        #             label=ft.Text("Origen", color= PRIMARY_BLUE),
        #             border_color=PRIMARY_BLUE,
        #         ),
        #         ft.TextField(
        #             label=ft.Text("Destino", color= PRIMARY_BLUE),
        #             border_color=PRIMARY_BLUE,
        #         ),
        #         ft.ElevatedButton(
        #             text="BUSCAR",
        #             color=MAIN_WHITE,
        #             bgcolor=PRIMARY_BLUE,
                    
        #         )
        #     ]
        # ),
    def build(self) -> ft.Column:
        return ft.Column(
            horizontal_alignment= ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    label=ft.Text("Origen", color= PRIMARY_BLUE),
                    border_color=PRIMARY_BLUE,
                ),
                ft.TextField(
                    label=ft.Text("Destino", color= PRIMARY_BLUE),
                    border_color=PRIMARY_BLUE,
                ),
                ft.ElevatedButton(
                    text="BUSCAR",
                    color=MAIN_WHITE,
                    bgcolor=PRIMARY_BLUE,
                    
                )
            ]
        ),