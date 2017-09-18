# schema for Rashberry pi

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (1000, 840)

Builder.load_file("main.kv")


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class NextScreen(Screen):
    pass


rashberry = ScreenManager()
rashberry.add_widget(MainScreen(name='menu'))
rashberry.add_widget(LoginScreen(name='login'))
rashberry.add_widget(NextScreen(name='next'))


class MyApp(App):
    def build(self):
        return rashberry

if __name__ == '__main__':
    MyApp().run()
