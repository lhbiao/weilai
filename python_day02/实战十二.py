print('在古希腊神话中，玫瑰集爱情与美丽于一身，所以人们常用玫瑰来表达爱情，但是不同朵数的玫瑰花代表的含义是不同的')
mount = int(input('请输入您想送我几朵玫瑰花，我会告诉玫瑰花的含义:'))
if mount == 1:
    print('%s朵:'%mount+'你是我的唯一')
elif mount == 3:
    print('%s朵:'%mount+'I Love You')
elif mount == 10:
    print('%s朵:'%mount+'十全十美')
elif mount == 99:
    print('%s朵:'%mount+'天长地久')
elif mount == 108:
    print('%s朵:'%mount+'求婚')
elif mount == 999:
    print('%s朵:'%mount+'土豪')
else: 
    print('其他')
