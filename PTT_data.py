import requests
from  bs4 import BeautifulSoup

# for pageno in range(1,10):
#     url = "https://www.ptt.cc/bbs/movie/index%s.html"%(pageno)
#     headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
#     res = requests.get(url, headers=headers)
#     soup = BeautifulSoup(res.text, "html.parser")
#     data_tags = soup.find_all("div",{"class":"title"})
#     for i, item in enumerate(data_tags):
#         print("Title : " + data_tags[i].a.text)
#         print("Link : https://www.ptt.cc" + data_tags[i].a["href"])
"====================================以下用Select改寫========================================="
# data_tags = soup.select("div[class='title']")
# for i, item in enumerate(data_tags):
#     print("Title : " + data_tags[i].a.text)
#     print("Link : https://www.ptt.cc/bbs/movie/" + data_tags[i].a["href"])
pageno = 9500
while(pageno >=9490):
    url = "https://www.ptt.cc/bbs/movie/index%s.html" % (pageno)
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    data_tags = soup.find_all("div", {"class": "title"})
    for i,item in enumerate(data_tags):
        try:
            print("Title : " + data_tags[i].a.text)
            print("Link : https://www.ptt.cc" + data_tags[i].a["href"])
        except AttributeError as e:
            print("This article might have been removed.")
    pageno -= 1