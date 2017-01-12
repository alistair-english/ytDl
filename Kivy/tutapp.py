import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class tutapp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(font_size=150, size_hint_y=0.5, text='default')
        f = FloatLayout()
        s = Scatter()
        l = Label(font_size=150, text='default')

        t.bind(text=l.setter('text'))

        f.add_widget(s)
        s.add_widget(l)
        b.add_widget(t)
        b.add_widget(f)

        return b
if __name__=='__main__':
    tutapp().run()
