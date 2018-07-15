print('查询能量请输入能量来源！退出程序请输入1:',end="\t")
print('能量来源如下:',end="\n")
print('行走捐、生活缴费、共享单车、线下支付、网络购票')
energy_source = input()
if energy_source == '0':
    print('已退出')
else:
    while str(energy_source) == '行走捐':
        print('200')
        break
    while str(energy_source) == '生活缴费':
        print('300')
        break
    while str(energy_source) == '共享单车':
        print('350')
        break   
    while str(energy_source) == '线下支付':
        print('380')
        break
    while str(energy_source) == '网络购票':
        print('500')
        break

