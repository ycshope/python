#python3.6 urllib
import requests

# api请求
# https://blog.csdn.net/weixin_32123093/article/details/113639153
if __name__ == "__main__":
    #login
    url = "http://www.meiduo.site:9000/login/"
    # url = "http://www.meiduo.site:9000/register/"
    data = {'username': 'shuner', 'password': '11111111', 'remembered': False}
    import json

    # dict 2 json
    jdata = json.dumps(data)
    try:
        res = requests.api.post(url=url, data=jdata, proxies="")
    except Exception as e:
        print("req error!!!")
    # print(f"header={res.headers}")
    cookie = res.headers.get('Set-Cookie')
    # b 2 josn
    content = res.content.decode()
    # json 2 dict
    body_dict = json.loads(content)
    code = body_dict.get('code')
    errmsg = body_dict.get('errmsg')
    print(f"code={code},errms={errmsg},cookie={cookie}")

    #cookie是一个字典序列,所有的header也都是字典序列
    cookie = {"sessionid": "qbnk86lkzw30moe5562k921ygg06z8j6"}
    try:
        res = requests.api.get(url="http://www.meiduo.site:9000/addresses/",
                               cookies=cookie)
    except Exception as e:
        print("req addr error!")
        exit(1)

    cnt = res.content.decode()
    print(json.loads(cnt))
