# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.clock import Clock

# class LongPressLabel(Label):
#     def __init__(self, **kwargs):
#         super(LongPressLabel, self).__init__(**kwargs)
#         self.long_press_duration = 1.0  # in seconds
#         self.long_press_triggered = False
#         self.long_press_clock = None
#         self.points = 0
#         self.final_points = 0
#         self.points_label = Label(text="Points: 0")
#         self.add_widget(self.points_label)

#     def on_touch_down(self, touch):
#         if self.collide_point(*touch.pos):
#             self.long_press_clock = Clock.schedule_interval(self.update_points, 0.1)
#             Clock.schedule_once(self.check_long_press, self.long_press_duration)
#         return super(LongPressLabel, self).on_touch_down(touch)

#     def on_touch_move(self, touch):
#         if not self.collide_point(*touch.pos):
#             self.cancel_long_press()
#         return super(LongPressLabel, self).on_touch_move(touch)

#     def on_touch_up(self, touch):
#         self.cancel_long_press()
#         return super(LongPressLabel, self).on_touch_up(touch)

#     def check_long_press(self, dt):
#         self.long_press_triggered = True
#         print("Long press detected")

#     def update_points(self, dt):
#         if self.long_press_triggered:
#             self.points += 1
#             self.points_label.text = f"Points: {self.points}"

#     def cancel_long_press(self):
#         if self.long_press_triggered:
#             print("Long press finished")
#             self.final_points = self.points
#         if self.long_press_clock:
#             self.long_press_clock.cancel()
#         self.long_press_triggered = False
#         self.long_press_clock = None
#         self.points = 0

# class LongPressApp(App):
#     def build(self):
#         return LongPressLabel(text="Long Press Me")

# if __name__ == "__main__":
#     LongPressApp().run()
#  def on_touch_down(self, touch):
#         if self.collide_point(*touch.pos):
#             #create if else separation of activated autotap and single presses
#             if self.switch_widget and self.switch_widget.active:
#                 # self.parent.parent.parent.points +=5
#                 # self.hp -= 1
#                 # if self.hp <= 0:
#                 #     self.new_donut()
#                 # if
#                 if touch.time_end - touch.time_start >= self.long_press_duration
                

#                     self.update_points(0) 
#                     self.long_press_clock = Clock.schedule_interval(self.update_points, 0.05)
#                     Clock.schedule_once(self.check_long_press, self.long_press_duration)
#                 else:
#                     self.parent.parent.parent.points +=1
#                     self.hp -= 1
#                     if self.hp <= 0:
#                         self.new_donut()
                
#                     x = self.x
#                     y = self.y
#                     anim = Animation(x=x-5, y = y-5, duration = 0.05) + \
#                         Animation(x=x, y = y, duration = 0.05)
#                     anim.start(self)
#                     self.is_anim = True
#                     anim.on_complete = lambda *args: setattr(self, 'is_anim', False)

#             else:
#                 self.parent.parent.parent.points +=1
#                 self.hp -= 1
#                 if self.hp <= 0:
#                     self.new_donut()
                
#                 x = self.x
#                 y = self.y
#                 anim = Animation(x=x-5, y = y-5, duration = 0.05) + \
#                     Animation(x=x, y = y, duration = 0.05)
#                 anim.start(self)
#                 self.is_anim = True
#                 anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
#         return super().on_touch_down(touch)
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class LongPressLabel(Label):
    def __init__(self, **kwargs):
        super(LongPressLabel, self).__init__(**kwargs)
        self.long_press_duration = 1.0  # in seconds
        self.long_press_triggered = False
        self.long_press_clock = None
        self.points = 0  # Total points accumulated
        self.points_label = Label(text="Points: 0")
        self.add_widget(self.points_label)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # Start updating points immediately to ensure no delay in counting
            self.update_points(0) 
            # if long press triggered do this - function for many points
            self.long_press_clock = Clock.schedule_interval(self.update_points, 0.05)
            Clock.schedule_once(self.check_long_press, self.long_press_duration)
            # else do this - function for 1 point
        return super(LongPressLabel, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            self.cancel_long_press()
        return super(LongPressLabel, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        self.cancel_long_press()
        return super(LongPressLabel, self).on_touch_up(touch)

    def check_long_press(self, dt):
        self.long_press_triggered = True
        print("Long press detected")

    def update_points(self, dt):
        if self.long_press_triggered:
            self.points += 1
            self.points_label.text = f"Points: {self.points}"
        
    def cancel_long_press(self):
        if self.long_press_triggered:
            print("Long press finished")
        if self.long_press_clock:
            self.long_press_clock.cancel()
        self.long_press_triggered = False
        self.long_press_clock = None
        # Do not reset points here to accumulate over multiple long presses

class LongPressApp(App):
    def build(self):
        return LongPressLabel(text="Long Press Me")

if __name__ == "__main__":
    LongPressApp().run()

# IDEA FROM GPT


# In your provided code, it looks like you intend to have a switch that controls some functionality (like toggling "autotap" or something similar) but didn't implement the switch correctly. To make the switch interactive and functional, you need to define the switch in the UI (preferably using Kivy's KV language for layout) and connect it to an action through Python code.

# Let's fix the missing parts, including the switch implementation and how to make it interactive:

# ### 1. Add a Switch to the `ShopScreen` Layout

# First, if you want to control something like an "autotap" feature with a switch, you need to properly define this switch in your interface. Since you didn't include the KV layout definition in your initial post, let's create a simple one.

# #### Add this KV definition in your Python script:

# This can be added right above your `MainApp` class.

# ```python
# from kivy.lang import Builder

# Builder.load_string("""
# <ShopScreen>:
#     BoxLayout:
#         orientation: 'vertical'
#         Label:
#             text: 'Toggle Auto-Tap'
#         Switch:
#             id: autotap_switch
#             active: False
#             on_active: root.toggle_autotap(args[1])

# <MenuScreen>:
#     BoxLayout:
#         Button:
#             text: 'Go to Game'
#             on_press: app.root.current = 'game'
#         Button:
#             text: 'Go to Shop'
#             on_press: app.root.current = 'shop'

# <GameScreen>:
#     BoxLayout:
#         orientation: 'vertical'
#         Button:
#             text: 'Back to Menu'
#             on_press: app.root.current = 'menu'
#         Label:
#             text: 'Points: ' + str(root.points)
#         Donut:
#             id: donut
#             source: 'assets/donuts/1.jpg'
# """)
# ```

# ### 2. Implement `toggle_autotap` method in `ShopScreen`

# In your `ShopScreen` class, you need to define the `toggle_autotap` function to make changes according to the switch state:

# ```python
# class ShopScreen(Screen):
#     autotap_active = False  # Track autotap state

#     def toggle_autotap(self, active):
#         self.autotap_active = active
#         print(f"Auto-Tap is now {'enabled' if active else 'disabled'}")
#         # You could add more functionality here to actually start/stop auto-tapping
# ```

# ### 3. Modify `Donut` to respond to autotap

# The `Donut` class should check if autotapping is enabled and then act accordingly. You can use the `Clock` to schedule/unschedule functions if autotapping is turned on/off. Here's an example of how to modify the `Donut` class:

# ```python
# class Donut(Image):
#     def on_touch_down(self, touch):
#         if self.collide_point(*touch.pos):
#             game_screen = self.parent.parent.parent
#             if game_screen.ids.shop_screen.autotap_active:  # Access the ShopScreen and check autotap
#                 # This assumes the GameScreen knows about ShopScreen; you may need to adjust based on actual structure
#                 self.auto_increment_points()
#             else:
#                 self.increment_points()
#             return True
#         return super().on_touch_down(touch)

#     def auto_increment_points(self):
#         # Handle continuous point incrementing if auto-tap is active
#         pass

#     def increment_points(self):
#         # Handle single point increment
#         pass
# ```

# ### 4. Ensure Proper Navigation and Initialization

# You also need to ensure that each screen can properly navigate to the others and that widgets are initialized correctly. For that, you have added navigation buttons in the KV definitions.

# ### Running Your App

# Now, your app should have a functional switch in the `ShopScreen` that toggles an "autotap" feature. Modify the `Donut` class and other parts of your application logic to fully integrate this functionality based on your app's requirements.