#kivy requirements
import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

from Libs.include import getSongs, download, getPafy

downloadPath = './Music/'


class SongListButton(ListItemButton):
    pass

class AttribDownloader(BoxLayout):
    songTextInput = ObjectProperty()
    artistTextInput = ObjectProperty()
    songList = ObjectProperty()

    def getSongsFromAttrib(self):
        song = self.songTextInput.text
        artist = self.artistTextInput.text
        urls = getSongs(song, artist)
        pafys = []
        for url in urls:
            pafy = getPafy(url)
            pafys.append(pafy)
            self.songList.adapter.data.extend([pafy.title])

        self.songList._trigger_reset_populate()




#links = getSongs(song, artist)
#get pafy objects for links and display the titles
#when one is selected send the pafy object to donwload function

#download(video, downloadPath)

class AttribDownloaderApp(App):
    def build(self):
        return AttribDownloader()
        #return Label(text='WHat the fuck is happeneing')

if __name__ == '__main__':
    AttribDownloaderApp().run()
