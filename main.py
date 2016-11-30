from Libs.include import getSongs, download

downloadPath = "./Music/"

toDownload = getSongs()

print("Downloading {0} song(s).".format(len(toDownload)))

for video in toDownload:
    download(video, downloadPath)
