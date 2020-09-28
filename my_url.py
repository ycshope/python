#python3.6 urllib
import urllib.request
  
def Get_Url(url,headers):
    request= urllib.request.Request(url,headers=headers)    #发送请求
    response = urllib.request.urlopen(request) 
    data = response.read()  #返回值是bytes类型
    print(data.decode('utf-8')) #需要解码呈str

if __name__ == "__main__":
    url = "https://10.63.0.100/"
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Connection" : "keep-alive"
    }
    url_html = Get_Url(url,headers)
    print(url_html)