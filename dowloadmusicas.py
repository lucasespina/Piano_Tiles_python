

# FAZENDO DOWNLOAD MÚSICAS YOUTUBE MP3 ---> programa acessório
from pytube import YouTube
import os

url = 'https://www.youtube.com/watch?v=4GSXyo3euR4'
yt = YouTube(url)
video = yt.streams.filter(only_audio=True).first()
downloaded_file = video.download()
base, ext = os.path.splitext(downloaded_file)
new_file = base + '.mp3'
os.rename(downloaded_file, new_file)
print("Done")





