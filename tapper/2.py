from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class SpinLabel(Label):
    angle = 0
    is_spinning = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(SpinLabel, self).__init__(**kwargs)
        self.start_spin_event = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.start_spin_event = Clock.schedule_once(self.start_spin, 5)
        return super(SpinLabel, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.start_spin_event:
            self.start_spin_event.cancel()
            self.start_spin_event = None
            if self.is_spinning:
                self.is_spinning = False
                self.text = "Press and hold to spin"
        return super(SpinLabel, self).on_touch_up(touch)

    def start_spin(self, dt):
        self.is_spinning = True
        self.text = "Spin started!"
        self.font_size = '20sp'
        self.center = self.parent.center
        self.rotate_event = Clock.schedule_interval(self.rotate, 0.1)

    def rotate(self, dt):
        self.angle += 1

class SpinLabelApp(App):
    def build(self):
        return SpinLabel(text="Press and hold to spin")
    #define through def

if __name__ == "__main__":
    SpinLabelApp().run()

