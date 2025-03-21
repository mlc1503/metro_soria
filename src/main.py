import flet as ft
from styles import *
import views.mainView as mainView
import views.buscarView as buscarView

def main(page: ft.Page):
    page.title = "Metro Soria"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

# TODO: STYLING
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = MAIN_WHITE
    

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary=PRIMARY_BLUE), 
        appbar_theme=ft.AppBarTheme(
            bgcolor=PRIMARY_BLUE,
            color= MAIN_WHITE,
        ), 
        elevated_button_theme=ft.ElevatedButtonTheme(
            bgcolor=PRIMARY_BLUE,
            foreground_color=MAIN_WHITE,
            shape= ft.RoundedRectangleBorder(radius=5), #TODO: no funciona(?), para que el border_round debe estar declarado en el propio ElevatedButton
        ),
    )

    APP_BACKGROUND_COLOR = MAIN_WHITE # todas las vistas estén con el color especificado como background, deben ponerse en todas las vistas del router

    # print("Initial route: ", page.route)

    appbarMS = ft.AppBar(
        title=ft.Text("Metro Soria", color=MAIN_WHITE),
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
                bgcolor=APP_BACKGROUND_COLOR,
                # padding=20
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
                    bgcolor=APP_BACKGROUND_COLOR
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