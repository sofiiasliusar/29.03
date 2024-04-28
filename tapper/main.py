from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.animation import Animation
from random import randint
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.switch import Switch

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
class GameScreen(Screen):
    points = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self, *args):
        donut = self.ids.donut
        donut.new_donut()
        donut.switch_widget = self.manager.get_screen('shop').ids.switch




class Donut(Image):
    hp = None
    long_press_clock = None
    switch_widget = ObjectProperty(None)
    long_press_duration = 2.0  # in seconds
    is_touch_down = False  # Flag to track if touch is down
    def check_touch_down(self):
        return self.collide_point(*Window.mouse_pos)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.is_touch_down = True  # Set touch down flag
            if self.switch_widget and self.switch_widget.active:
                Clock.schedule_once(self.handle_single_tap, 0)
                Clock.schedule_once(self.check_press, self.long_press_duration)
            else:
                self.handle_single_tap()
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.is_touch_down = False  # Clear touch down flag
        if self.long_press_clock:
            self.long_press_clock.cancel()
            self.long_press_clock = None
        return super().on_touch_up(touch)

    def check_press(self, dt):
        if self.check_touch_down():
            if self.long_press_clock:
                self.long_press_clock.cancel()
            self.handle_long_press()
        elif self.long_press_clock:
            self.long_press_clock.cancel()
            self.long_press_clock = None


    def handle_single_tap(self, dt=None):
        if self.is_touch_down:  # Only increment points if touch is down
            self.parent.parent.parent.points += 1
            self.hp -= 1
            if self.hp <= 0:
                self.new_donut()
            x = self.x
            y = self.y
            anim = Animation(x=x-5, y=y-5, duration=0.05) + Animation(x=x, y=y, duration=0.05)
            anim.start(self)

    def handle_long_press(self):
        if not self.is_touch_down:
            if self.long_press_clock:
                self.long_press_clock.cancel()
                self.long_press_clock = None
            return
        self.long_press_clock = Clock.schedule_interval(self.update_points, 0.05)

    def update_points(self, dt):
        if self.is_touch_down:  # Only increment points if touch is down
            self.parent.parent.parent.points += 1
            self.hp -= 1
            if self.hp <= 0:
                self.new_donut()

    def new_donut(self):
        app = App.get_running_app()
        self.donut = app.LEVELS[randint(0, len(app.LEVELS)) - 1]
        self.source = app.DONUTS[self.donut]['source']
        self.hp = app.DONUTS[self.donut]['hp']


class ShopScreen(Screen):
    def init(self, **kwargs):
        super().__init__(**kwargs)
    def autotap(self, active):
        if active:
            print("Switch activated")
            #
            return True #use it in donut for pressing if true: search from gpt
        else:
            print("Switch deactivated")
            #
            return False
    

class MainApp(App):
    LEVELS = ['1', '2', '3', '4', '5', '6']
    DONUTS = {
        '1': {"source": 'assets/donuts/1.jpg', 'hp': 10},
        '2': {"source": 'assets/donuts/2.jpg', 'hp': 20},
        '3': {"source": 'assets/donuts/3.jpg', 'hp': 30},
        '4': {"source": 'assets/donuts/4.jpg', 'hp': 40},
        '5': {"source": 'assets/donuts/5.png', 'hp': 50},
        '6': {"source": 'assets/donuts/6.jpg', 'hp': 60}
    }
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name = 'menu'))
        sm.add_widget(GameScreen(name = 'game'))
        sm.add_widget(ShopScreen(name = 'shop'))
        return sm

    if platform != 'android':
        Window.size = (400,800)
        Window.left = 750
        Window.top = 100
app = MainApp
app().run() 