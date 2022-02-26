from os import system
from easygui import msgbox,buttonbox,enterbox
from sys import exit
from time import sleep
exttime = 3
windowtitle='BetterHTMLHelp KagamineRin1.02 '
while True:
    mode = buttonbox('您要如何访问？', windowtitle, ('百度', '图片', '自己输入网址','退出'))
    if mode == '百度':
        content = enterbox('你想搜索什么？',windowtitle)
        system(r'hh http://www.baidu.com/s?wd='+content)
    elif mode == '图片':
        msgbox('已经打开image.baidu.com。请在网站中搜索。',windowtitle)
        system(r'hh http://image.baidu.com/')
    elif mode == '自己输入网址':
            content = enterbox('你想搜索什么？',windowtitle)
            system(r'hh http://'+content)
            msgbox('网址合规。 已开启！',windowtitle+' 网页已经开启！')
    elif mode == '退出':
        exit()
