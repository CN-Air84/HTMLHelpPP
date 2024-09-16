import os
import sys
import easygui
windowtitle='BetterHTMLHelp KagamineRin1.01 '
while True:

    mode = easygui.buttonbox('您要如何访问？', windowtitle, ('百度', '图片', '自己输入网址','退出'))
    if mode == '百度':
        content = easygui.enterbox('你想搜索什么？',windowtitle)
        os.system(r'hh http://www.baidu.com/s?wd='+content)
    elif mode == '图片':
        easygui.msgbox('已经打开image.baidu.com。请在网站中搜索。',windowtitle)
        os.system(r'hh http://image.baidu.com/')
    elif mode == '自己输入网址':
            content = easygui.enterbox('你想搜索什么？',windowtitle)
            os.system(r'hh http://'+content)
            easygui.msgbox('网址合规。 已开启！',windowtitle+' 网页已经开启！')
    elif mode == '退出':
        break

    
        
    
    
