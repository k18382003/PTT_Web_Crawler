import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
import os
import requests
from bs4 import BeautifulSoup

# root window
root = tk.Tk()
root.title('PTT電影版爬蟲')
var = tk.StringVar()
var2 = tk.StringVar()
root.resizable(False, False)

strFilePath = tk.StringVar()

def getFilePath():
    FilePath = tk.filedialog.askdirectory()
    if(FilePath!=''):
        strFilePath.set(FilePath)

def fetch_content(pagestart, pageend, savepath):
    resource_path = savepath
    if not os.path.exists(resource_path):
        os.makedirs(resource_path)

    while(pageend >= pagestart):
        url = "https://www.ptt.cc/bbs/movie/index%s.html" % (pageend)
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        data_tags = soup.select("div[class='title']")
        for item in data_tags:
            try:
                article_headline = item.a.text
                article_link = "https://www.ptt.cc" + item.a["href"]
                headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
                res = requests.get(article_link, headers=headers)
                soup = BeautifulSoup(res.text, "html.parser")
                article_content = soup.select("div[id='main-content']")[0].text.split("--")[0]
                # 將內容載下來
                with open(r'%s/%s.txt' % (resource_path, article_headline.replace(':', ' ')), 'w', encoding="UTF-8") as w:
                    w.write(article_content)
            except AttributeError as e:
                print(e)
            except FileNotFoundError as e:
                pass
            except OSError as e:
                pass
        pageend -= 1
    tk.messagebox.showinfo('下載結果', '已下載完畢')


# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# temperature label
lblcrawlpage = ttk.Label(frame, text='想要爬取的頁數')
lblrange = ttk.Label(frame, text='從~到:')
lblfilepath = ttk.Label(frame, text='存檔路徑:')
lblcrawlpage.grid(column=0, row=0, sticky='W')
lblrange.grid(column=0, row=1, sticky='W')
lblfilepath.grid(column=0, row=2, sticky='W')


# temperature entry
start = tk.StringVar()
start_entry = ttk.Entry(frame, textvariable=start)
start_entry.grid(column=1, row=1)
end = tk.StringVar()
tilda = ttk.Label(frame, text='~')
tilda.grid(column=2, row=1, sticky='W')
end_entry = ttk.Entry(frame, textvariable=end)
end_entry.grid(column=3, row=1)
start_entry.focus()

filepath_button = ttk.Button(frame, text='存檔路徑', command=getFilePath)
filepath_button.grid(column=0, row=2, sticky='W')
filepath_input = ttk.Entry(frame, textvariable=strFilePath, width=45)
filepath_input.grid(columnspan=3, column=1, row=2, sticky='W')

def Trigger_Fetch():
    startpage = int(start.get())
    endpage = int(end.get())
    saveFilePage = strFilePath.get()
    fetch_content(startpage, endpage, saveFilePage)

confrim_button = ttk.Button(frame, text='開始爬文', command=Trigger_Fetch)
confrim_button.grid(column=3, row=4, sticky='W')

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()