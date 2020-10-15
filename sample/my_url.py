#python3.6 urllib
import urllib.request
  
def Get_Url(url):
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Connection" : "keep-alive"
    }
    
    request = urllib.request.Request(url,headers=headers)    #发送请求

    try: #"尝试"
        response = urllib.request.urlopen(request)
    except Exception as e:    #失败结果
        print("url error!")
        print(e)
        return None
    
    data = response.read()  #返回值是bytes类型
    return(data.decode('utf-8')) #需要解码呈str

if __name__ == "__main__":
    url = "http://www.hitsz.edu.cn/index.html"
    url_html = Get_Url(url)
    print(url_html)