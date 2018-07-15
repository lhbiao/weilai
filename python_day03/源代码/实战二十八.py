age = int(input('请输入您的年龄:'))
subject = input('请输入您的专业:')
collge = input('请回答您的大学是否为重点大学:')
#while (age >= 25 and age <= 28) or (subject == '计算机专业' or collge == '电子信息工程') or (collge == '重点大学'):
    
if (age >= 25 and subject == '电子信息工程') or (subject == '电子信息工程' and collge == '是') or (age <= 28 and subject == '计算机专业'):
    print('恭喜您达到面试资格')
        
else:
    print('抱歉,您未达到面试要求')

