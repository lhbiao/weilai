a = {'中心':32,'音乐模块':30,'微信支付模块':42}
print('------跳一跳,请输入\"退出"即可退出游戏-----\n欢迎回来,请开始游戏\n请输入(中心、音乐模块、微信支付模块)')
while True:
    Input = input('请输入:')
    if Input == '退出':
        print('已退出')
        break
    elif Input in a:
        print('您的分数为:%d'%a[Input])
    else:
        print('输入有误,请重新输入')
