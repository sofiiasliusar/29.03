# 1 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
# core відповідає за ОС
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.animation import Animation
from random import randint
# 2
class MenuScreen(Screen):
    def __init__(self, **kwargs):
# змінна буде розпаковуватись **словник *список
        super().__init__(**kwargs)
        
class GameScreen(Screen):
    points = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_enter(self, *args):
        self.ids.donut.new_donut()

class Donut(Image):
    is_anim = False
    hp = None
    donut = None
    donut_index = 0
    
    def on_touch_down(self, touch):
        # self.source = "assets/1.jpg"
        if self.collide_point(*touch.pos):
            self.parent.parent.parent.points +=1
            self.hp -= 1
            if self.hp <= 0:
                self.new_donut()
                
            x = self.x
            y = self.y
            anim = Animation(x=x-5, y = y-5, duration = 0.05) + \
                Animation(x=x, y = y, duration = 0.05)
            anim.start(self)
            self.is_anim = True
            anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
        return super().on_touch_down(touch)
    def new_donut(self):
        self.donut = app.LEVELS[randint(0, len(app.LEVELS))-1] #index 8 number 9
        self.source = app.DONUT[self.donut]['source'] #CONSTANTS
        self.source = app.DONUT[self.donut]['hp']
        
class MainApp(App):
    #LEVELS
    #PLANETS
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name = 'menu'))
        sm.add_widget(GameScreen(name = 'game'))
        return sm

    if platform != 'android':
        Window.size = (400,800)
        Window.left = 750
        Window.top = 100
app = MainApp
app().run()