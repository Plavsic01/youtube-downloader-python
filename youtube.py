from __future__ import unicode_literals
from pydub import AudioSegment
import youtube_dl
import glob,os

class Youtube:
    def __init__(self,path) -> None:
        self.txtfiles = []
        self.path = path
        os.chdir(self.path)

    def downloadAndSearch(self):
        ydl_opts = {"format":"mp4"}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls) #mora biti lista

        for file in glob.glob(self.path+"/*.mp4"): #"/Users/andrej/Desktop/python/youtube/*.mp4"
            self.txtfiles.append(file)

    def newFormat(self):
        for i in range(len(self.txtfiles)):
            src = self.txtfiles[i]
            dst = self.txtfiles[i].replace(".mp4","") + ".mp3"
            sound = AudioSegment.from_file(src)
            sound.export(dst, format="mp3")
            os.remove(self.txtfiles[i])


#where to download files
path = input("Enter path where you want to download files...\n")
# Creating Youtube class
yt = Youtube(path)
#urls => links from youtube to download
urls = input("enter one or more urls, separated with commas(,) :\n").split(",")
# Calling method on the Youtube object, for downloading and searching through directory
yt.downloadAndSearch()
# Calling method to format to wanted file format
yt.newFormat()

