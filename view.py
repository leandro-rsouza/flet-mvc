import flet as ft

class UserView:
    def __init__(self, page):
        self.page = page
        self.page.title = "Cadastro e Login"
        self.username = ft.TextField(label="Username")
        self.password = ft.TextField(label="Password", password=True)

    def show_login(self, login_callback):
        self.page.controls.clear()
        self.page.add(
            ft.Column([
                self.username,
                self.password,
                ft.ElevatedButton("Login", on_click=login_callback),
                ft.TextButton("Registrar", on_click=lambda e: self.show_register())
            ])
        )
        self.page.update()

    def show_register(self, register_callback=None):
        self.page.controls.clear()
        self.page.add(
            ft.Column([
                self.username,
                self.password,
                ft.ElevatedButton("Registrar", on_click=register_callback),
                ft.TextButton("Voltar", on_click=lambda e: self.show_login())
            ])
        )
        self.page.update()

    def show_message(self, message):
        self.page.add(ft.Text(message))
        self.page.update()