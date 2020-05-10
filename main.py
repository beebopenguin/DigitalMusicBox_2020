from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Triangle


class NoteScreen(Screen):
    pass


class TempoScreen(Screen):
    pass


class TriangleButton(ButtonBehavior, Triangle):
    on_press: print("hi")


class InstrumentScreen(Screen):
    pass


class MainApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrumentScreen(name='instruments'))
        sm.add_widget(TempoScreen(name='tempo'))
        sm.add_widget(NoteScreen(name='notes'))

        return sm


if __name__ == '__main__':
    MainApp().run()