# 1 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
# core відповідає за ОС
from kivy.utils import platform

# 2
class MenuScreen(Screen):
    def __init__(self, **kwargs):
# змінна буде розпаковуватись **словник *список
        super().__init__(**kwargs)
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name = 'menu'))
        sm.add_widget(GameScreen(name = 'game'))
        return sm

    if platform != 'android':
        Window.size = (400,800)
        Window.left = 750
        Window.top = 100
MainApp().run()