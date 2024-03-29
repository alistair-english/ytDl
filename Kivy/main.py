import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class MainApp(App):
    def build(self):
        main = BoxLayout(orientation='vertical', height=800)
        grid = GridLayout(cols=1)
        title = Label(text='ytDl', size_hint_y=None, height=200, font_size=150)
        songLabel = Label(text='Song:', size_hint_y=None, height=150, font_size=100)
        artistLabel = Label(text='Artist:',  size_hint_y=None, height=150, font_size=100)
        song = TextInput(multiline=False, size_hint_y=None, height=100, font_size=80)
        artist = TextInput(multiline=False, size_hint_y=None, height=100, font_size=80)
        download = Button(text='Download', size_hint_y=None, height=100, font_size=80)

        grid.add_widget(title)
        grid.add_widget(songLabel)
        grid.add_widget(song)
        grid.add_widget(artistLabel)
        grid.add_widget(artist)
        grid.add_widget(download)
        main.add_widget(grid)

        return main

if __name__=='__main__':
    Window.size = (500, 800)
    MainApp().run()
