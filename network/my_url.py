#python3.6 urllib
import urllib.request
import urllib.parse
    
def Get_Url(url):
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Connection" : "keep-alive"
    }
    
    request = urllib.request.Request(url,headers=headers)    #发送请求

    try: #"尝试"
        response = urllib.request.urlopen(request,timeout=1) ##设置超时时间为0.1秒,将抛出异常
    except Exception as e:    #失败结果
        print("url error!")
        print(e)
        return None
        
    #返回的code
    code = response.status
    #print(code)
    #return code
    if code == 200:
    #返回网页,返回值是bytes类型,需要解码呈str
        data = response.read()
        context = data.decode('utf-8')
        return context
    else:
        return code
    #返回的请求头
    #res_header = response.info()
    #return res_header
    '''
    #返回的cookies
    import http.cookiejar
    cookie=http.cookiejar.CookieJar() #实例化cookiejar对象
    handler=urllib.request.HTTPCookieProcessor(cookie) #构建一个handler
    opener=urllib.request.build_opener(handler) #构建Opener
    response=opener.open(url) #请求
    #print(cookie)
    for item in cookie:
        print(item.name+"="+item.value)
    '''

if __name__ == "__main__":
    url = "http://www.dudj.net/hongsejingdian/53/"
    
    start = 1596
    end = 1669
    i = start
    import time
    while i <= end:
        #遍历的html拼凑
        t_url = url + str(i) + ".html"
        url_body = Get_Url(t_url)
        print(f"body={url_body}")
        print(f"url = {t_url}")
        i += 1
        #time.sleep(1)
        