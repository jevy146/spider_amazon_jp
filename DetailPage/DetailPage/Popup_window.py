# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 15:01
# @Author  : 结尾！！
# @FileName: Popup_window.py
# @Software: PyCharm


# import ctypes
# # ctypes.windll.user32.MessageBoxA(0,'Scrapy Close！','infomation',4)
# MessageBox = ctypes.windll.user32.MessageBoxA
# message='Scrapy Close！'
# MessageBox(None, message, 'Install as a Service', 0)
# msg = ctypes.windll.user32.MessageBoxA(0,'python 你好！','弹框',0)

# import thinter
# from tkinter import messagebox
# # print("这是一个弹出提示框")
# messagebox.showinfo("提示","我是一个提示框")

'''https://blog.csdn.net/weixin_39416561/article/details/84190336'''
# import win32api,win32con
# win32api.MessageBox(0, "这是一个测试提醒OK消息框", "提醒",win32con.MB_OK)

# from selenium import webdriver
# browser=webdriver.Chrome()
#
# browser.get('https://www.amazon.co.jp/')

ranking= ['\n',
             'Amazon 売れ筋ランキング:',
             ' \n\n\n\n\n\n\n\n\n\n\n\n\n\nホーム＆キッチン - 75,101位 (',
             'ホーム＆キッチンの売れ筋ランキングを見る',
             ')\n \n\n\n\n\n\n',
             '\n'
             '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; }\n'
             '.zg_hrsr_item { margin: 0 0 0 10px; }\n'
             '.zg_hrsr_rank { display: inline-block; width: 80px; text-align: '
             'right; }\n',
             '\n\n',
             '\n    ',
             '\n    ',
             '49位',
             '\n    ',
             '─\xa0',
             'スチームクリーナー',
             '\n    ',
             '\n',
             '\n\n']

ranking2 = [each.strip() for each in ranking if each.strip() != '']
print(ranking2)