import flet as ft
from styles import *
import views.mainView as mainView
import views.holaView as holaView


def main(page: ft.Page):
    page.title = "Metro Soria"

    # print("Initial route: ", page.route)

    appbarMS = ft.AppBar(title=ft.Text("Metro Soria"))

    # def route_change(e):
    #     print("Change route to: ", e.route)
    #     page.views.clear()
    #     page.views.append(
    #         ft.View(
    #             "/",
    #             [
    #                 appbarMS,
    #                 mainView.drawUI()
    #             ],
    #         )
    #     )
    #     if page.route == "/hola":
    #         page.views.append(
    #             ft.View(
    #                 "/hola",
    #                 [
    #                     appbarMS,
    #                     holaView.draw()
    #                 ]
    #             )
    #         )
    #     page.update()

    #     def view_pop(e):
    #         print("View pop:", e.view)
    #         page.views.pop()
    #         top_view = page.views[-1]
    #         page.go(top_view.route)

    #     page.on_route_change = route_change
    #     page.on_view_pop = view_pop


    # page.go(page.route)
    # page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/hola")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        if page.route == "/hola":
            page.views.append(
                ft.View(
                    "/hola",
                    [
                        appbarMS,
                        holaView.draw()
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