from flet import app
from controller import UserController

def main(page):
    controller = UserController(page)
    controller.start()

app(target=main)