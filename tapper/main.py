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
    is_anim = False
    hp = None
    donut = None
    donut_index = 0
    long_press_clock = None
    switch_widget = ObjectProperty(None)
    long_press_duration = 1.0  # in seconds
    long_press_triggered = False
    long_press_clock = None
    
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.touch_start_time = Clock.get_time()
            
            #create if else separation of activated autotap and single presses - to do
            if self.switch_widget and self.switch_widget.active: #tried saying and when more than 1 sec
                # also here tried
                # self.update_points(0) 
                # self.long_press_clock = Clock.schedule_interval(self.update_points, 0.05)
                # Clock.schedule_once(self.check_long_press, self.long_press_duration)
                self.long_press_clock = Clock.schedule_interval(self.update_points, 0.05)
                Clock.schedule_once(self.check_long_press, self.long_press_duration)
                if self.long_press_triggered:

                    self.handle_long_press()
                else:
                    self.handle_single_tap()
            else:
                self.handle_single_tap()
                # self.parent.parent.parent.points +=1
                # self.hp -= 1
                # if self.hp <= 0:
                #     self.new_donut()
                
                # x = self.x
                # y = self.y
                # anim = Animation(x=x-5, y = y-5, duration = 0.05) + \
                #     Animation(x=x, y = y, duration = 0.05)
                # anim.start(self)
                # self.is_anim = True
                # anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
        return super().on_touch_down(touch)
    
    def handle_long_press(self):
        self.update_points(0) 
        self.long_press_clock = Clock.schedule_interval(self.update_points, 0.05)
        Clock.schedule_once(self.check_long_press, self.long_press_duration)

    def handle_single_tap(self):
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
    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            self.cancel_long_press()
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        # a = Clock.get_time() - self.touch_start_time
        # print(a)
        self.cancel_long_press()
        return super().on_touch_up(touch)

    def check_long_press(self, dt):
        # tried to do it only for when more than one second = true, but didn`t work
        self.long_press_triggered = True
        print("Long press detected")

    def update_points(self, dt):
        if self.long_press_triggered:
            self.parent.parent.parent.points +=1
            self.hp -= 1
            if self.hp <= 0:
                self.new_donut()
        
    def cancel_long_press(self):
        if self.long_press_triggered:
            print("Long press finished")
        if self.long_press_clock:
            self.long_press_clock.cancel()
        self.long_press_triggered = False
        self.long_press_clock = None

    def new_donut(self):
        self.donut = app.LEVELS[randint(0, len(app.LEVELS))-1] #index 8 number 9
        self.source = app.DONUTS[self.donut]['source'] #CONSTANTS
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