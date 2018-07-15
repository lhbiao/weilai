number = 1001
# bai_wei = number // 100
# shi_wei = (number // 10) % 10
# ge_wei = number % 10
# Sum = bai_wei**3 + shi_wei**3 + ge_wei**3 
while number >= 100:
    bai_wei = number // 100
    shi_wei = (number // 10) % 10
    ge_wei = number % 10

    if number == bai_wei**3 + shi_wei**3 + ge_wei**3:
        print('水仙花数是:%d'%number)
       
    number -= 1


 
