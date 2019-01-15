from urllib.request import urlopen
from bs4 import BeautifulSoup

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


li_list = ul_songs.find_all("li")
# print(li_list)

songs_list = []
li = li_list[0]

# print(li)

for li in li_list:
    h4 = li.h4

print(h4)