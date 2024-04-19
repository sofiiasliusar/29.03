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
            self.long_press_clock = Clock.schedule_interval(self.update_points, 0.1)
            Clock.schedule_once(self.check_long_press, self.long_press_duration)
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
