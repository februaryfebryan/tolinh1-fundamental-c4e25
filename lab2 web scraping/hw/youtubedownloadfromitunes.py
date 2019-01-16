from youtube_dl import YoutubeDL
from urllib.request import urlopen
from bs4 import BeautifulSoup
# from collections import OrderedDict
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"

# 1. Download the page
conn = urlopen(url)

raw_data = conn.read ()

content = raw_data.decode()


f = open("itunes.html", "wb") #wb = write binary
f.write(raw_data)
f.close()

#2. Find ROI

soup = BeautifulSoup(content, "html.parser")
# content = soup.find_all('li')[2]
ul_songs = soup.find_all("ul")[3]

#3. Copy and save
# print(ul_songs.prettify())

li_list = ul_songs.find_all("li")
# print(li_list)

# #TÌM NAME VÀ ARTIST
# songs_list = []
li = li_list[0]

# print(li)

new_list = []
for li in li_list:
    h4 = li.h4
    h3 = li.h3
    # print(h3)
     
    a = h4.a
    a1 = h3.a
    # print(a1)

    artist = a.string
    songname = a1.text
    

    # print(songname)




    options = {
        'default_search': 'ytsearch', 
        'max_downloads': 1, 
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([songname])