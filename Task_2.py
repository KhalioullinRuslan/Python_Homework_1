# Задача 2: Найдите сумму цифр трехзначного числа.

print('Введите трехзначное число: ')
number = input()
sum = 0
if len(str(number)) == 3:
    for i in range(len(number)):
        sum += int(number[i])
    print(sum)
else:
    print('Не подходящее число')