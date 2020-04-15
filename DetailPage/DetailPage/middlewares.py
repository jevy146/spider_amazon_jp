# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging

from scrapy import signals


class DetailpageSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



from fake_useragent import UserAgent
import json
import time

import base64
    # 代理服务器
# proxyServer = "http://http-cla.abuyun.com:9030"
#
# # 代理隧道验证信息
# proxyUser = "H7V9P9Q694L32B5C"
# proxyPass = "52F8CF6FBAE70F68"


    # for Python3
# proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

# proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


'''使用动态版隧道'''
# proxyServer = "http://http-dyn.abuyun.com:9020"
# proxyUser = "HIX9H33N87639FSD"
# proxyPass = "580D452C7B02267E"

# proxyServer = "http://http-cla.abuyun.com:9030"
# proxyUser = "H7V9P9Q694L32B5C"
# proxyPass = "52F8CF6FBAE70F68"
#  proxyServer = "http://http-pro.abuyun.com:9010"
# 代理隧道验证信息


# proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         request.meta["proxy"] = proxyServer
#
#         request.headers["Proxy-Authorization"] = proxyAuth










'''使用socks5 代理 '''
from stem import Signal
from stem.control import Controller
import socket
import socks
import requests
import time
controller = Controller.from_port(port=9151)  # 9151
controller.authenticate()
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)  # 8123是在浏览器中设置的，  9150
# socket.socket = socks.socksocket
# ip = requests.get("http://checkip.amazonaws.com").text
# print("替换IP：", ip)  # 查看包装的IP是
# controller.signal(Signal.NEWNYM)




class DetailpageDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.



    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s


    # def read_cookies(self):
    #
    #     with open(r"F:\envs_pycharm\做分布式-美国\使用socket的美国\DetailPage\DetailPage\cookies.txt", "r") as fp:
    #         cookies = json.load(fp)
    #         cookie = [item["name"] + ":" + item["value"] for item in cookies]
    #         cookMap = {}
    #         for elem in cookie:
    #             str = elem.split(':')
    #             cookMap[str[0]] = str[1]
    #         print(f"在CookiesMiddleware使用的cookMap = {cookMap}")
    #         return cookMap


    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called


        # cookies = self.read_cookies()
        # cookie_jar = cookies
        # # print("cookie_jar", cookie_jar)
        # request.cookies = cookie_jar


        ua = UserAgent()
        USER_AGENT = ua.chrome # 任意头文件
        # print(USER_AGENT)
        request.headers['User-Agent'] = USER_AGENT



        '''使用socket5 作为代理'''

        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)  # 8123是在浏览器中设置的，  9150
        socket.socket = socks.socksocket
        #使用Tor代理,只能保存为csv文件
        ip = requests.get("http://checkip.amazonaws.com").text
        print("使用IP：", ip)  # 查看包装的IP是 61.238.105.146 本地

        # proxy='127.0.0.1:9150'
        # proxies={
        #     'http:':'socks5://'+proxy,
        #     'https:':'socks5://'+proxy,
        #
        # }
        # request.meta["proxy"] = proxies

        # socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)  # 8123是在浏览器中设置的，  9150
        # socket.socket = socks.socksocket

        #从selenium中手动改邮编之后复制所得，直接复制的也可以
        # Cookie_Copy = 'session-id=355-6614492-8783445; i18n-prefs=JPY; ubid-acbjp=358-1525158-7840910; x-wl-uid=11Z8nB/Fz6E8zJUCKjQ423L8B/IaHm3Xh2Pw2guxNW5/wthdeyUf1Qa5xXpYGOxxB1XUNAhp2lV0=; cdn-session=AK-91120dacb76bac627037851815990142; skin=noskin; session-token=GtxLMDrlp1disK4TJayvmAd+8k41b33X+G8okC+UCaFbZm7O9YNew+citRQ8M5u0isrxLKQMf7gTxA2BoYroQJUySB25Pec0i/kBryZTBhMTzdvTU22Npz7uRS2GALyVhkZZ+3VbGH1zdfNHM79jtV8Ertz/1xRs5hD1CGkpMklOH5oXbTMrlbWjaaU2MEyi; x-amz-captcha-1=1586602191538115; x-amz-captcha-2=BMl9V5WnZDQ0cdOVxGEmPQ==; session-id-time=2082726001l; csm-hit=tb:7Y2KVD4W2ESV5WJHWRGP+s-EK0GQRPS7HGR63FGQV51|1586596026704&t:1586596026704&adb:adblk_no'
        # cookie_dict = {i.split("=")[0]: i.split("=")[1] for i in Cookie_Copy.split("; ")}
        # request.cookies = cookie_dict
        request.cookies = {
            'session-id':'355-6614492-8783445',
            'session-id-time':'2082726001l',

        }
        logging.debug('Using headers:%s' % request)



        '''增加阿布云代理'''
        # request.meta["proxy"] = proxyServer
        # print("正常增加IP", proxyAuth)
        # request.headers["Proxy-Authorization"] = proxyAuth
        # logging.debug('Using Proxy:%s' % proxyServer)


        '''使用芝麻代理'''
        # ip_dict=crawl_xdaili()
        # proxies = {
        #     'http': 'http://' + ip_dict['ip']+':'+ip_dict['port'],
        #     'https': 'https://' +  ip_dict['ip']+':'+ip_dict['port']
        # }
        # print(proxies)
        # proxies='https://' +'58.218.92.150:5238'
        # request.meta["proxy"] = proxies


        print('request.header',request.headers)


        return None



    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        print('DownloaderMiddleware返回状态码：', response.status)


        ip = requests.get("http://checkip.amazonaws.com").text
        print("替换IP：", ip)  # 查看包装的IP是
        controller.signal(Signal.NEWNYM)

        return response


    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain

        # print('代理%s，访问 %s 出现异常:%s' % (request.meta['proxy'], request.url, exception))

        time.sleep(1)

        ua = UserAgent()
        USER_AGENT = ua.chrome  # 任意头文件
        print('出错了',USER_AGENT)
        request.headers['User-Agent'] = USER_AGENT

        # request.meta["proxy"] = proxyServer
        # print("正常增加IP", proxyAuth)
        # request.headers["Proxy-Authorization"] = proxyAuth
        return request
        # pass


    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)





#
# from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
# from scrapy.selector import HtmlXPathSelector
# from scrapy.utils.response import get_meta_refresh
# from scrapy import log
#
# class CustomRetryMiddleware(RetryMiddleware):
#
#     def process_response(self, request, response, spider):
#         url = response.url
#         if response.status in [301, 307]:
#             log.msg("trying to redirect us: %s" %url, level=log.INFO)
#             reason = 'redirect %d' %response.status
#             return self._retry(request, reason, spider) or response
#         interval, redirect_url = get_meta_refresh(response)
#         # handle meta redirect
#         if redirect_url:
#             log.msg("trying to redirect us: %s" %url, level=log.INFO)
#             reason = 'meta'
#             return self._retry(request, reason, spider) or response
#         hxs = HtmlXPathSelector(response)
#         # test for captcha page
#         captcha = hxs.select(".//input[contains(@id, 'captchacharacters')]").extract()
#         if captcha:
#             log.msg("captcha page %s" %url, level=log.INFO)
#             reason = 'capcha'
#             return self._retry(request, reason, spider) or response
#         return response










'''Python http/sock5:

#coding=utf-8
import requests

#请求地址
targetUrl = "http://baidu.com"

#代理服务器
proxyHost = "ip"
proxyPort = "port"

proxyMeta = "http://%(host)s:%(port)s" % {

    "host" : proxyHost,
    "port" : proxyPort,
}

#pip install -U requests[socks]  socks5代理
# proxyMeta = "socks5://%(host)s:%(port)s" % {

#     "host" : proxyHost,

#     "port" : proxyPort,

# }

proxies = {

    "http"  : proxyMeta,
}

resp = requests.get(targetUrl, proxies=proxies)
print resp.status_code
print resp.text

'''

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
#         ip_dict=random.choice(proxies_list)
#         print(ip_dict)
#         return ip_dict
