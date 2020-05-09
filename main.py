from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyButton(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'Images\AcousticGuitar.jpg'

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'Images\Button_down.jpg'
        else:
            self.source = 'Images\AcousticGuitar.jpg'


class ImageButton(ToggleButtonBehavior, Image):
    pass


class InstrumentScreen(Screen):
    pass


class MainApp(App):

    def build(self):
        return InstrumentScreen()
        #return MyButton()


if __name__ == '__main__':
    MainApp().run()