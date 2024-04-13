# create auto tap when switch is on - integrate comment code and read about it
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
from kivy.clock import Clock
# 2
class MenuScreen(Screen):
    def __init__(self, **kwargs):
# змінна буде розпаковуватись **словник *список
        super().__init__(**kwargs)
        
class GameScreen(Screen):
    points = NumericProperty(0)
    # The constructor takes arbitrary keyword arguments (**kwargs). 
    # This allows the class to accept any additional arguments
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.donut = Donut(game_screen_ref=self)

    # This line calls the constructor of the parent class (Screen) using super(). 
    # It passes any keyword arguments received by the GameScreen constructor to the parent class constructor. 
    def on_enter(self, *args):
        self.ids.donut.new_donut()
        # accesses the ids dictionary of the GameScreen instance. 
        # In Kivy, the ids dictionary contains references to all widgets declared in the KV language file associated with the screen




class Donut(Image):
    is_anim = False
    hp = None
    donut = None
    donut_index = 0
    autotap = False  # Variable to track autotap state
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_screen_ref = kwargs.get('game_screen_ref') 
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.autotap or touch.is_mouse_scrolling:  # Check if autotap is enabled or scrolling
                self.game_screen_ref.points += 1  # Access points from GameScreen instance
                self.hp -= 1
                if self.hp <= 0:
                    self.new_donut()
                    
                x = self.x
                y = self.y
                anim = Animation(x=x-5, y=y-5, duration=0.05) + \
                    Animation(x=x, y=y, duration=0.05)
                anim.start(self)
                self.is_anim = True
                anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
            return True  # Return True to indicate that the touch event is consumed
        return super().on_touch_down(touch)
    
    def new_donut(self):
        self.donut = app.LEVELS[randint(0, len(app.LEVELS))-1]
        self.source = app.DONUTS[self.donut]['source']
        self.hp = app.DONUTS[self.donut]['hp']
        
        if self.autotap:
            Clock.schedule_interval(self.auto_increment_points, 0.1)  # Start autotapping
        
    def auto_increment_points(self, dt):
        self.parent.parent.parent.points += 1
        self.hp -= 1
        if self.hp <= 0:
            self.new_donut()

class ShopScreen(Screen):
    def init(self, **kwargs):
        super().__init__(**kwargs)
    def toggle_autotap(self, active):
        self.ids.autotap_switch.autotap = active 

    
    def on_touch_down(self, touch):
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
        self.source = app.DONUTS[self.donut]['source'] #CONSTANTS
        self.hp = app.DONUTS[self.donut]['hp']
        
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

# auto - tap

# from kivy.app import App
# from kivy.uix.image import Image
# from kivy.properties import NumericProperty
# from kivy.animation import Animation
# from kivy.clock import Clock
# from random import randint
# from kivy.uix.screenmanager import ScreenManager, Screen

# class Donut(Image):
#     is_anim = False
#     hp = None
#     donut = None
#     donut_index = 0
#     points_increment = 1

#     def on_touch_down(self, touch): 
#         if self.collide_point(*touch.pos):
#             if not touch.ud.get('point_added', False):  # Check if the point has already been added for this touch
#                 self.parent.parent.parent.points += self.points_increment
#                 touch.ud['point_added'] = True  # Set the flag to indicate that the point has been added
#                 self.schedule_points_increment()  # Start scheduling points increment
#             self.hp -= 1
#             if self.hp <= 0:
#                 self.new_donut()
                
#             x = self.x
#             y = self.y
#             anim = Animation(x=x-5, y=y-5, duration=0.05) + Animation(x=x, y=y, duration=0.05)
#             anim.start(self)
#             self.is_anim = True
#             anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
#         return super().on_touch_down(touch)
    
#     def on_touch_up(self, touch):
#         if touch.ud.get('point_added', False):
#             touch.ud.pop('point_added')  # Reset the flag when touch is released
#             Clock.unschedule(self.increment_points)  # Stop scheduling points increment if the flag was set
#         return super().on_touch_up(touch)

#     def schedule_points_increment(self):
#         Clock.schedule_interval(self.increment_points, 0.1)
    
#     def increment_points(self, dt):
#         self.parent.parent.parent.points += self.points_increment
    
#     def new_donut(self):
#         self.donut = app.LEVELS[randint(0, len(app.LEVELS))-1]
#         self.source = app.DONUTS[self.donut]['source']
#         self.hp = app.DONUTS[self.donut]['hp']

# class GameScreen(Screen):
#     points = NumericProperty(0)
    
#     def on_enter(self, *args):
#         self.ids.donut.new_donut()

# class MenuScreen(Screen):
#     pass

# class MainApp(App):
#     LEVELS = ['1', '2', '3', '4', '5', '6']
#     DONUTS = {
#         '1': {"source": 'assets/donuts/1.jpg', 'hp': 10},
#         '2': {"source": 'assets/donuts/2.jpg', 'hp': 20},
#         '3': {"source": 'assets/donuts/3.jpg', 'hp': 30},
#         '4': {"source": 'assets/donuts/4.jpg', 'hp': 40},
#         '5': {"source": 'assets/donuts/5.png', 'hp': 50},
#         '6': {"source": 'assets/donuts/6.jpg', 'hp': 60}
#     }
    
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(MenuScreen(name='menu'))
#         sm.add_widget(GameScreen(name='game'))
#         return sm

# if __name__ == '__main__':
#     app = MainApp()
#     app.run()
