import requests
import pafy
import sys
import os
import re
from ffmpy import FFmpeg
from html.parser import HTMLParser
from subprocess import call

#======HTML Parser for the links======
class Parser(HTMLParser):
    def initLinks(self):
        self.links = []
    def handle_starttag(self, tag, attrs):
        if(tag == "a"):
            for attr in attrs:
                if(attr[0] == "href"):
                    if(attr[1].startswith("/watch?")):
                        self.links.append(attr[1])
    def cleanLinks(self):
        links = []
        for i in range(0, len(self.links), 2):
            links.append("http://www.youtube.com" + self.links[i])
        self.links = links

#======A method for taking input========
#takes in the normal prompt, then a list of values or value type to check the input against
#and an optional message to display when the
def safeInput(prompt, values, wrongMsg="Invalid Input.\n"):
    if(type(values)==type):
        while True:
            try:
                return values(input(prompt))
            except ValueError:
                print(wrongMsg, end="")
    else:
        while True:
            inp = input(prompt)
            for val in values:
                try:
                    if(type(val)(inp) in values):
                        return type(val)(inp)
                except ValueError:
                    pass
            print(wrongMsg, end="")



#======Take input and return a list of songs to download======
def getSongs():
    prompts = [["Song: ", "Artist: "], ["URL: "]]
    option = safeInput("(1) Song and Artist, (2) URL: ", [1, 2]) - 1
    #note: test url by doing a get_playlist and then catching valueErrors
    values = {prompts[option][i].replace(": ", ""): input(prompts[option][i]) for i in range(len(prompts[option]))}

    if(option==0):
        print("Getting page...")
        html = requests.get("http://www.youtube.com/results?search_query={0}+{1}+audio".format(values["Artist"], values["Song"])).text

        print("Parsing...")
        parser = Parser()
        parser.initLinks()
        parser.feed(html)
        parser.cleanLinks()
        links = parser.links

        for link in links:
            vid = pafy.new(link)
            if safeInput("Downloading '{0}'. Continue? (y/n): ".format(vid.title), str) in "yY":
                return [vid]
        #if we get here we've go no more videos
        print("No more videos in the list... Exiting.")
        sys.exit()
    elif(option==1):
        try:
            playlist = pafy.get_playlist(values["URL"])
            return [item['pafy'] for item in playlist['items']]
        except ValueError:
            return [pafy.new(values["URL"])]

#======Download a pafy object to a filePath======
def download(vid, path):
    print("'{}'".format(vid.title))
    best = vid.getbestaudio()
    search = re.compile(r'\*|\.|"|\/|\\|\[|\]|:|;|\||=|,|@|[^\x00-\x7F]')
    title = search.sub("", vid.title)
    filePath = best.download(filepath=path + title)
    print("\nComplete.\nConverting to MP3...")
    #call(["ffmpeg", "-loglevel", "warning", "-i", "{0}".format(filePath), "{0}".format(path + title + ".mp3")])
    FFmpeg(inputs={"{0}".format(filePath):None}, outputs={"{0}".format(path + title + ".mp3"):None}).run()
    print("Complete.\nCleaning up...")
    os.remove(filePath)
    print("Complete.")
