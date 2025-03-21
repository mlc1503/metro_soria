import flet as ft
from styles import *
import views.mainView as mainView
import views.buscarView as buscarView


def main(page: ft.Page):
    page.title = "Metro Soria"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    print("Initial route: ", page.route)

    appbarMS = ft.AppBar(
        title=ft.Text("Metro Soria"),
        bgcolor=PRIMARY_BLUE,
        
        )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    appbarMS,
                    mainView.draw(page) #por cada vista que hay, debemos pasarle el objeto Page del main para que haga el routing
                ],
            )
        )
        if page.route == "/buscar":
            page.views.append(
                ft.View(
                    "/buscar",
                    [
                        appbarMS,
                        buscarView.draw(page)
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)