eigh = int(input('请输入身高:  cm'))
price = int(input('请输入身价:    W$'))
face = int(input('请输入颜值分:   分'))
if heigh >= 180 and price >= 1000000 and face >= 99:
   print('恭喜，你是高富帅')
elif heigh < 180 and price >= 1000000 and face >= 99:
   print('恭喜，你是富帅')
elif heigh < 180 and price < 1000000 and face >= 99:
   print('帅')
elif heigh < 160 and price <100 and face <60:
   print('矮矬穷')
