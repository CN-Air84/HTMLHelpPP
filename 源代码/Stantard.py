from os import system
from easygui import msgbox,buttonbox,enterbox
windowtitle='BetterHTMLHelp KagamineRin1.01'

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
            if 'baidu.com' in content and 'http://' not in content and 'https://' not in content:
                system(r'hh http://'+content)
                msgbox('网址合规。 已开启！',windowtitle+' 网页已经开启！')
            elif 'http://' in content or 'https://' in content:
                msgbox('网址不合规：输入的网址中带有http://或https://。',windowtitle+'网页不合规!')
            else:
                msgbox('网址不合规：域名不在白名单中 ',windowtitle+'网页不合规！')
    elif mode == '退出':
        break

    
        
    
    
