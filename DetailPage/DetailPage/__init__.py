# def start_requests(self):
#     cls = self.__class__
#     if method_is_overridden(cls, Spider, 'make_requests_from_url'):
#         warnings.warn(
#             "Spider.make_requests_from_url method is deprecated; it "
#             "won't be called in future Scrapy releases. Please "
#             "override Spider.start_requests method instead (see %s.%s)." % (
#                 cls.__module__, cls.__name__
#             ),
#         )
#         for url in self.start_urls:
#             yield self.make_requests_from_url(url)
#     else:
#         for url in self.start_urls:
#             yield Request(url, dont_filter=True)
#
#
# def make_requests_from_url(self, url):
#     """ This method is deprecated. """
#     return Request(url, dont_filter=True)
#
# '''https://blog.csdn.net/qq_40717846/article/details/79014132  研究一下知乎的分布式'''

#
# import random,time
# print(random.random()*10)
# print('11111',random.randrange(1,4,1))
# print('11111',random.randint(1,4))
# print(round(random.random()+random.randint(1,4), 1) )
# import random
# import numpy as np
#
# a = random.randint(10, 20)
# res = np.random.randn(5)
# ret = random.random()
# print("正整数:" + str(a))
# print("5个随机小数:" + str(res))
# print("0-1随机小数:" + str(ret))

# import requests
# import json
# import random
# def crawl_xdaili():
#     """
#     获取讯代理
#     :return: 代理
#     """
#     url = 'http://http.tiqu.alicdns.com/getip3?num=20&type=2&pro=&city=0&yys=0&port=1&pack=71846&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'
#     html = requests.get(url)
#     print(html)
#     if html:
#         result = json.loads(html.text)
#         proxies_list = result.get('data')
#         ip=random.choice(proxies_list)
#         print(ip)
#
#
# crawl_xdaili()
# from fake_useragent import UserAgent
# ua = UserAgent()
# USER_AGENT = ua.random # 任意头文件
# print(USER_AGENT)