# 设定账号：98766 密码：123456 金额：1000
count = int(input('请输入账号'))
passwd = int(input('请输入密码'))
if count != 98765 or passwd != 123456:
    print('非法账户')
else:
    print('请输入取款金额：')
money = int(input())
b = 1000 - money
if money <= 1000:
    print('您好，您取了%d元'%money+'剩余%d元'%b)
else:
    print('没钱取毛线啊')
