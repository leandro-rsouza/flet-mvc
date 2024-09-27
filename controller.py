from model import Database
from view import UserView

class UserController:
    def __init__(self, page):
        self.db = Database(host='localhost', user='root', password='', database='mvc')
        self.view = UserView(page)

    def login(self, e):
        username = self.view.username.value
        password = self.view.password.value
        user = self.db.find_user(username)

        if user and user[2] == password:  # Assume que a senha está na terceira coluna
            self.view.show_message("Login bem-sucedido!")
        else:
            self.view.show_message("Usuário ou senha incorretos.")

    def register(self, e):
        username = self.view.username.value
        password = self.view.password.value

        if self.db.find_user(username):
            self.view.show_message("Usuário já existe.")
        else:
            self.db.create_user(username, password)
            self.view.show_message("Usuário registrado com sucesso.")

    def start(self):
        self.view.show_login(self.login) # É aqui que o erro: Somente apresenta a inserção de dados para login -> show_login(self.login)