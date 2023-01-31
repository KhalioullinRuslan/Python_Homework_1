# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.


print('Введите номер билета: ')
Ticketnumber = str(input())
firstNumber = 0
secondNumber = 0
if len(Ticketnumber) != 6:
    print('Не подходящее число')
elif len(Ticketnumber) == 6:
    for i in range(3):
        firstNumber += int(Ticketnumber[i])
        secondNumber += int(Ticketnumber[i + 3])
    if firstNumber == secondNumber:
        print('Это счастливый билет)')
    else:
        print('Это обычный билет')