from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#urllib
url = "https://dantri.com.vn"

# 1. Download the page

#1.1 Open connection
conn = urlopen(url)

#1.2 Read data
raw_data = conn.read()

#1.3 Decode data
content = raw_data.decode("utf8")  #utf8 là dành cho các trang web không phải là tiếng anh

# print(content)

# f = open("dantri.html", "wb") #wb = write binary
# f.write(raw_data)
# f.close()

# 2. Find ROI 

#Cài tool beautiful souppip
soup = BeautifulSoup(content, "html.parser") #beautiful soup sẽ hiểu đây là một file html
ul_news = soup.find("ul", "ul1 ulnew") #dùng để tìm ROI chính xác chỉ có một cái
# print(ul_news.prettify()) #thêm prettify để nhìn rõ được cái nào là bố cái nào là con
# 3. Copy n save

li_list = ul_news.find_all("li")   
# li = li_list[0]   #Trong một list nhiều soup thì tìm 1 soup đẻ có thể làm việc được
news_list = []
for li in li_list:
    #ĐANG TÌM TITLE VÀ LINK

    #walking technique 
    h4 = li.h4 #để đi dần từ h4 đến a
    # print(h4)

    a = h4.a
    print(a)
#     link = url + a["href"] #là dictionary               # thêm url + để trông giống một cái link
#     title = a.string

#     # print(title, link)
#     # print("--------------")

#     news = OrderedDict({
#         "title": title,
#         "link": link                   #gộp lại thành dictionary
#     })

#     # print(news)

#     news_list.append(news)

# # print(news_list)

# #Cài tool pip install pyexcel
# #cài tool pip install pyexcel xlsx để hỗ trợ việc đọc xlsx và xls
# #Mở https://github.com/pyexcel/pyexcel để đọc usage

# pyexcel.save_as(records = news_list, dest_file_name = "dantri1.xls")