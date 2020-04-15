# -*- coding: utf-8 -*-
import base64

import scrapy
from scrapy.selector import Selector
from DetailPage.items import DetailpageItem
import copy
import random
from scrapy_redis.spiders import RedisSpider



'''使用标椎格式框架写的分布式爬虫，设置redis_key,框架会自动从数据库中提取对列发送请求。'''
import json


import time

# import socket
# import socks
import redis


class UsaDetailSpider(RedisSpider):
    name = 'Detail'
    allowed_domains = ['amazon.co.jp']
    handle_httpstatus_list = [302]
    # start_urls = ['http://www.amazon.ca/']

    redis_key = "Detail:start_urls"

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(UsaDetailSpider, self).__init__(*args, **kwargs)

    def make_requests_from_url(self, url):

        print('****开始******',url)

        if 'primevideo' in url:
            pass
        else:

            return scrapy.Request(url,
                dont_filter = True)


    def parse(self, response):  #不写start_urls了

        if response.status == 302:  #谷歌浏览器出现url重定向的问题，验证cookie，将url引到其他第链接了
            return

        commodity_info = DetailpageItem()
        if response.status == 200:
            selector = Selector(response)
            commodity_info["ASIN"] = response.url .split("/")[-1]  # 商品ASIN
            try:
                address = selector.xpath('//*[@id="glow-ingress-line2"]/text()').extract_first()  # 获取邮编的地址，，
                print("查看详情页的邮编。", address)  # 查看邮编地址。。。
            except:
                address="null"
            # print("查看第二次邮编。", address)
            try:
                commodity_item = selector.xpath('//*[@id="productTitle"]/text()').extract_first().replace("\n"," ").strip()  # 商品名称 将.strip()去掉了。
            except:
                commodity_item="null"

            print("产品",commodity_item)
            if address ==None :
                # print(response.text)
                if 'Robot Check' in response.text or commodity_item=="null":
                    '''将数据保存到redis重新爬取'''
                    print('有验证码。。。',response.url)
                    URL=response.url
                    conn = redis.Redis(host='192.168.31.104', port=6379, )
                    conn.lpush('Detail:start_urls', URL)
                    print('将链接重新加入到redis数据库中', URL)
                    time.sleep(random.randint(2,5))

                    import win32api,win32con
                    win32api.MessageBox(0, "帅哥  scrapy爬虫 自动关闭", "提醒",win32con.MB_OK)
                    self.crawler.engine.close_spider(self, '有验证码，主动关闭爬虫')
                    return


            if commodity_item=="null" :
                print("产品为空，，程序结束")
                ''' 判断是那种大海报类型的详情页，，程序结束。'''
                return

            commodity_info["commodity_item"] = commodity_item  # 商品名称

            try:
                brandName = selector.xpath('//a[@id="bylineInfo"]/text()').extract_first()  # 品牌名称
            except:
                brandName = "null"
            commodity_info["brandName"] = brandName  # 品牌卖家
                #print(111, brandName)
            try:
                price = selector.xpath('//*[@id="priceblock_dealprice"]/text()').extract_first()  # 并去掉特殊字符。。

                if price:
                    # print("正常。。。")
                    pass
                else:
                    # print("价格位置··",price)  #price=None，，
                    price = selector.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first()
                    if price:
                        pass
                    else:
                        price = selector.xpath(
                            '//*[@id="olp_feature_div"]//span[@class="a-color-price"]/text()').extract_first()

                price="".join(price.split())  #去掉\xa0
            except:

                price = "null"

            commodity_info["price"] = price  # 商品价格


            #评论数
            try:
                comments = selector.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first()  # 评论数
            except:
                comments = "null"

            commodity_info["comments"] = comments  # 品论数量

            #星级
            try:
                star_level = selector.xpath('//*[@id="reviewsMedley"]//span[@class="a-declarative"]/a/span/text()').extract_first()  # 星级 第二种写法，在页面上面的星级。
            except:
                star_level = 'null'

            commodity_info["star_level"] = star_level  # 品论数量

            '''tr标签，获取日期和排名，第1种，通过将所有的tr标签都获取下来，进行数据清洗 '''
            '''切记将tbody标签去掉,tbody标签是浏览器自动补全的，源代码是没有的'''
            '''https://www.amazon.co.jp/dp/B072PSCWYG>
             https://www.amazon.co.jp/dp/B082KHK4H5
             https://www.amazon.co.jp/dp/B07JVMTQDX
            
            '''
            try:
                login_information = selector.xpath(
                    '//*[@id="prodDetails"]//div[@class="column col2 "]//tr/td//text()').extract()

                if len(login_information)==0:
                    login_information = selector.xpath(
                        '//*[@id="productDetailsTable"]//ul//li//text()').extract()
                    if len(login_information) == 0:
                        login_information = selector.xpath(
                            '//*[@id="detail_bullets_id"]/table//ul//li//text()').extract()

                login_information = [each.strip() for each in login_information if each.strip() != '']
            except:
                login_information = 'null'
            commodity_info["login_information"] = login_information


            try:
                desc_information = selector.xpath(
                    '//*[@id="prodDetails"]//div[@class="pdTab"]//td//text()').extract()
                desc_information= [each.strip() for each in desc_information if each.strip() != '']

            except:
                desc_information='null'
            commodity_info['desc_information']=desc_information


            '''获取类目排名及详情页链接'''
            try:
                ranking = selector.xpath('//*[@id="SalesRank"]//text()').extract()
                ranking= [each.strip() for each in ranking if each.strip() != '']
            except:
                ranking='null'
            commodity_info['ranking']=ranking

            try:
                ranking_href = selector.xpath('//*[@id="SalesRank"]//a/@href').extract()
            except:
                ranking_href='null'
            commodity_info['ranking_href']=ranking_href

            try:
                img_src = selector.xpath('//*[@id="imgTagWrapperId"]//@src').extract()[0].strip()
                # print('img_src_1', img_src)
            except:
                img_src = selector.xpath('//*[@id="landingImage"]/@src').extract()[0].strip()
                # print('img_src_2', img_src)
            # img_src = selector.xpath('//*[@id="landingImage"]/@src').extract()[0]
            # print('img_src', img_src)
            # # str2 = img_src.split(',')[-1]
            # img_data = base64.b64decode(str2)
            commodity_info['img'] = img_src #保存图片完整的的链接。
            yield commodity_info




'''            tr_list_3=selector.xpath('//*[@id="productDetails_detailBullets_sections1"]//tr[6]//text()').extract()  #输出ASIN 和ASIN码
'''
