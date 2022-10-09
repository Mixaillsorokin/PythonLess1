# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#  Пример:
# 6 -> да
# 7 -> да
# 1 -> нет
# *Напишите программу, которая принимает на вход 2 числа: номер месяца и номер дня в месяце, проверяет является ли день выходным.
# Принимаем начало года на понедельник и считая год не високосным. Учитываем только гос праздники (НГ, 9 мая и т.д.)

Num1 = int(input('Введите число дня: '))
Num2 = int(input('Введите число месяца: '))
if (Num1>31 or Num2>12) or (Num1>31 and Num2==1)or (Num1>28 and Num2==2)or (Num1>31 and Num2==3)or (Num1>30 and Num2==4)or (Num1>31 and Num2==5)or (Num1>30 and Num2==5)or (Num1>30 and Num2==6)or (Num1>30 and Num2==6)or (Num1>31 and Num2==7)or(Num1>31 and Num2==8)or (Num1>30 and Num2==9)or(Num1>31 and Num2==10)or (Num1>30 and Num2==11)or(Num1>31 and Num2==12):
    print('Такого дня нет')
elif 1 <= Num1 <= 8 and Num2 == 1:
    print('Новогодние праздники c 1 января по 8 января!!!')
elif (Num1==21 or Num1==22 or Num1==28 or Num1==29) and (Num2==1):
    print('Выходной день')
elif (23 <= Num1 <= 26) and (Num2==2):
    print('23 февраля-День защитника отечества!отдыхаем до 26 февраля ')
elif (Num1 == 4 or Num1 == 5 or Num1 == 11 or Num1 == 12 or Num1 == 18 or Num1 ==19) and (Num2 == 2):
    print("Выходной день")
elif Num1 == 8 and Num2 == 3:
    print('Международный женский день') 
elif  (Num1 == 4 or Num1 == 5 or Num1 == 11 or Num1 == 12 or Num1 == 18 or Num1 ==19 or Num1 == 25 or Num1 ==26) and (Num2 == 3):
    print("Выходной день")
elif (29 <= Num1 <= 30) and (Num2 == 4):
    print("Праздник")
elif(Num1 == 1 or Num1 == 2 or Num1 == 8 or Num1 == 9 or Num1 == 15 or Num1 ==16 or Num1 == 22 or Num1 ==23) and (Num2 == 4):
    print("Выходной день")
elif(Num1 == 1 or 6<= Num1 <=9 )and (Num2 ==5):
    print("Праздник")
elif(Num1 == 13 or Num1 == 14 or Num1 ==20 or Num1 ==21 or Num1 ==27 or Num1 ==28) and (Num2 ==5):
    print("Выходной день")
elif(Num1 ==10 or Num1 == 11 or Num1 ==12)and (Num2==6):
    print("Праздник")
elif(Num1 ==3 or Num1 ==4 or Num1 ==17 or Num1 ==18 or Num1 ==24 or Num1 ==25)and (Num2==6):
    print("Выходной день")
elif(Num1 ==1 or Num1 ==2 or Num1 ==8 or Num1 ==9 or Num1 ==15 or Num1 ==16 or Num1 ==22 or Num1 ==23 or Num1 ==29 or Num1 ==30)and (Num2 ==7):
    print(" Выходной день")
elif (Num1==5 or Num1==6 or Num1==12 or Num1==13 or Num1==19 or Num1 ==20 or Num1 ==26 or Num1 ==27) and (Num2 ==8):
    print("Выходной день")
elif(Num1==2 or Num1==3 or Num1==9 or Num1==10 or Num1==16 or Num1==17 or Num1 ==23 or Num1 ==24 or Num1==30) and (Num2 ==9):
    print("Выходной день")
elif (Num1==1 or Num1==7 or Num1==8 or Num1==14 or Num1 ==15 or Num1==21 or Num1==22 or Num1==28 or Num1==29 )and (Num2 ==10):
    print("Выходной день")
elif (Num1 ==4 or Num1==5 or Num1==6 ) and (Num2 ==11):
    print("Праздник")
elif (Num1 ==11 or Num1==12 or Num1==18 or Num1==19 or Num1==25 or Num1==26) and (Num2 ==11):
    print("Выходной день")
elif (Num1 ==2 or Num1==3 or Num1==9 or Num1 ==10 or Num1 ==16 or Num1 ==17 or Num1 ==23 or Num1 ==24 or Num1 ==30 or Num1 ==31)and (Num2 ==12):
    print("Выходной день")
else:
    print('Будний день')