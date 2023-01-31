# Найдите сумму цифр любого вещественного или целого числа. 
# Можно использовать decimal. Через строку решать нельзя.

n = input('Введите число: ')
 
summ = 0
 
for digit in n:
    if digit.isdigit():
        summ += int(digit)
         
print("Сумма:", summ)

