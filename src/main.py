import flet as ft
from styles import PRIMARY_BLUE, PRIMARY_CYAN, SECONDARY_CYAN, ALERT_RED, MAIN_BLACK, MAIN_WHITE, SLIGHT_BLUE



def main(page: ft.Page):
    page.title = "Metro Soria"

    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            ft.View(
                route= '/',
                controls=[
                    
                    ft.AppBar(
                        title=ft.Text("Hola", color= MAIN_WHITE),
                        bgcolor=PRIMARY_BLUE,
                    ),
                    ft.Column(
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
                ]
            )
        )

        if page.route == '/lineas':
            page.views.append(
                ft.View(
                    route= '/lineas', 
                    controls=[
                        ft.Text("colega estamos en lineas")
                    ]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(main)
