import random
computer = random.randint(1,10)
player = int(input('玩家请出数'))
if player == computer:
   print('胜利')
else:
   print('失败，你是一个loser')

