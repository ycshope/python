from bs4 import BeautifulSoup
#BeautifulSoup是直接针网页的标签进行查找
#参考文档https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
import urllib.request

url = "http://td.sangfor.com/#/defect/problem"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Connection" : "keep-alive"
    }

request = urllib.request.Request(url , headers=headers)

#请求url
try:
    response = urllib.request.urlopen(request)
except Exception as e:
    print("url open error")
    print(e)
#解析成XML
soup = BeautifulSoup(response , "lxml")
#寻找标签a
pack_list = soup.find_all(name='a')

for pack in pack_list:
    #直接输出pack,那么会连同标签一起输出
    print(pack.string)