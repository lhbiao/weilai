birthday = int(input('请闰土输入您的出生年份：'))
if birthday % 4 == 0 and birthday % 100 != 0:
   print('闰土是闰年出生')
elif birthday % 400 == 0:
   print('闰土是闰年出生')
else:
   print('闰土是平年出生')
