dayWeek = int(input("введите день недели в формате от 1 до 7 :"))
while dayWeek<=0 or dayWeek>=8:
    dayWeek = int(input("введите день недели в формате от 1 до 7 :"))
if dayWeek>5:
    print('выходной')
else: print ('рабочий')
