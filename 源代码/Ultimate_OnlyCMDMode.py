from os import system
from time import sleep
#函数
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
while True:
    CMDenterbox('您要如何访问互联网？请输入对应的功能代码：\n百度 ;bd           图片 ;pic \n自定义网址 ;cus    退出 ;ext','BetterHTMLHelp KagamineRin1.01 ','在这里输入代码')
    if enterOutput == ';bd':
        CMDenterbox('你想搜索什么？','BetterHTMLHelp KagamineRin1.02 ')
        system(r'hh http://www.baidu.com/s?wd='+enterOutput)
        ez_msgbox('已开启！')
    elif enterOutput == ';pic':
        CMDmsgbox('请在确认后自行搜索！','已开启')
        system(r'hh http://image.baidu.com/')
    elif enterOutput == ';cus':
        CMDenterbox('你想搜索什么？', 'BetterHTMLHelp KagamineRin1.02 ','')
        system(r'hh http://' + enterOutput)
        ez_msgbox('已开启！')
    elif enterOutput == ';ext':
        for i in range(3):
            ez_msgbox('程序将在'+str(exttime)+'秒后退出！')
            sleep(1)
            exttime = exttime - 1
        break






    
