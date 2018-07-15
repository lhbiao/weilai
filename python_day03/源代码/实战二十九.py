chicken = 1
while chicken <= 30:
    rabbit = 30-chicken
    if 2*chicken+(30-chicken)*4 == 90:
        print('鸡有%d只'%chicken,'兔有%d只'%rabbit)
        break 
    chicken += 1

