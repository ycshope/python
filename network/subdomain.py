'''
某个网站的子域名:如baidu.com的子域名:aa.baidu.com bb.baidu.com
子域名搜索的方法:
    1.暴力破解:字典+域名
    2.搜索引擎:site:baidu.com
    3.网页爬取:主页中可能有带子域名的连接
    4.第三方查询:dig
    5./crossdomain.xml:域名后+/crossdomain.xml（sample:www.baidu.com/crossdomain.xml）
    6.https证书
    
程序选择6种的组合:方法1依赖于字典,方法2可以直接爬，方法3可以用正则表达式,方法4考虑用api，方法5不一定适用,方法6可以用api。
最后记得要去重；

设计思路：6种方法可以并行,用多进程解决。
'''