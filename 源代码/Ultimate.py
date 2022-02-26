from os import system
from easygui import msgbox,buttonbox,enterbox
from sys import exit
from time import sleep
#CMDMode 函数，初始化准备
def clearCMD(n=50):
    for i in range(n):
        print('\n')
def CMDmsgbox(text='text',title='title',windowlong=20):
    system(r'color 17')
    for wl in range(0,windowlong):
        if wl == windowlong-1:
            print('—')
        else:
            print('—',end='')
    printtext = windowlong-len(text)
    printtext = printtext/2
    printtext2 = int(printtext)
    printtext2 = printtext2 - 1
    printtext3 = windowlong-2
    print(title)
    for wl in range(0,windowlong):
        if wl == windowlong-1:
            print('—')
        else:
            print('—',end='')
    print(printtext3*'  ')
    print('  '*printtext2,text,'  '*printtext2)
    print(printtext3*'  ')
    for wl in range(0,windowlong):
        if wl == windowlong-1:
            print('—')
        else:
            print('—',end='')
    for wl in range(0,windowlong):
        if wl == windowlong-1:
            print('—')
        else:
            print('—',end='')
    input('按下Enter以确认。')
    clearCMD()
enterOutput = ''
def CMDenterbox(text='text',title='title',inputTips='input',windowlong=20):
    system(r'color 17')
    for wl in range(0,windowlong):
        if wl == windowlong-1:
            print('—')
        else:
            print('—',end='')
    printtext = windowlong-int(len(text))
    printtext = printtext/2
    printtext2 = int(printtext)
    printtext2 = printtext2 - 1
    printtext3 = windowlong-2
    print(title)
    for wl in range(0,windowlong):
        if wl == windowlong-1:
            print('—')
        else:
            print('—',end='')
    print(printtext3*'  ')
    print('  '*printtext2,text,'  '*printtext2)
    print(printtext3*'  ')
    for wl in range(0,windowlong):
        if wl == windowlong-1:
            print('—')
        else:
            print('—',end='')
    for wl in range(0,windowlong):
        if wl == windowlong-1:
            print('—')
        else:
            print('—',end='')
    global enterOutput
    enterOutput = input(inputTips)
    clearCMD()
def ez_msgbox(text='text'):
    print('————————————————————')
    print(text)
    print('————————————————————')
exttime = 3
windowtitle='BetterHTMLHelp KagamineRin1.03 '
windowmode=buttonbox('窗口显示模式？', windowtitle, ('[复古]CMD显示', '[现代]窗口显示',))
if windowmode == '[复古]CMD显示':
    while True:
        CMDenterbox('您要如何访问互联网？请输入对应的功能代码：\n百度 ;bd           图片 ;pic \n自定义网址 ;cus    退出 ;ext',
                    'BetterHTMLHelp KagamineRin1.03 ', '在这里输入代码')
        if enterOutput == ';bd':
            CMDenterbox('你想搜索什么？', 'BetterHTMLHelp KagamineRin1.03 ')
            system(r'hh http://www.baidu.com/s?wd=' + enterOutput)
            ez_msgbox('已开启！')
        elif enterOutput == ';pic':
            CMDmsgbox('请在确认后自行搜索！', '已开启')
            system(r'hh http://image.baidu.com/')
        elif enterOutput == ';cus':
            CMDenterbox('你想搜索什么？', 'BetterHTMLHelp KagamineRin1.03 ', '')
            system(r'hh http://' + enterOutput)
            ez_msgbox('已开启！')
        elif enterOutput == ';ext':
            for i in range(3):
                ez_msgbox('程序将在' + str(exttime) + '秒后退出！')
                sleep(1)
                exttime = exttime - 1
            for ii in range(30):
                clearCMD(1)
                sleep(0.1)
            system(r'color 07')
            ez_msgbox('已经退出！')
            sleep(1)
            break
    exit()
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
        ez_msgbox('3s后退出程序！')
        sleep(3)
        exit()
