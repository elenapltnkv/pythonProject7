#Задание №1:
#Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

# print('Привет! давай знакомиться!')
# name = input('Как тебя зовут?')
# print('Рад видеть тебя ', name)
# let= int(input('а сколько тебе лет? '))
# age= 18
# if let == age:
#     print('можем читать анекдоты')
# else:
#     print('тебе рано. может мультики?')

#Задание №2:
#Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
#выведите в формате чч:мм:сс. Используйте форматирование строк.
#1д = 3600 м = 1ч = 60 мин = 60 сек
# a=int(input())
# h=a//3600
# m=(a//60)%60
# s=a%60

# time = int(input('Введите время в секундах: '))
# convertTimeHour = time//3600
# print(convertTimeHour)
# convertTimeMinutes = (time//60)%60
# print(convertTimeMinutes)
# convertTimeSeconds = time%60
# print(convertTimeSeconds)
# timeA = ["{} hours {} mins {} seconds".format(convertTimeHour, convertTimeMinutes, convertTimeSeconds)]
# timeB = ['{:02d}:{:02d}:{:02d}'.format(convertTimeHour, convertTimeMinutes, convertTimeSeconds)]
# print(timeA)
# print(timeB)

# Задание №3:
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.
# chislo = (input("Введите число: "))
# buk = int(chislo)
# buk2=int(chislo+chislo)
# buk3 =int(chislo+chislo+chislo)
# result = buk+buk2+buk3
# print(result)
# print('Считаем '+ chislo+'+'+(chislo+chislo)+'+'+(chislo+chislo+chislo)+'=', result)

#Задание №4:
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# num = int(input('Введите число: '))
# while (num<100):
#     num+=1
#     print('наибольшее число', num)

#Задание №5:
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток —
# издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


vyruchka= int(input('Введите сумму выручки: '))
izderjka = int(input('Введите сумму издержки: '))
pribyl = vyruchka- izderjka
ubytoc = izderjka - vyruchka

if pribyl>ubytoc:
    print('В этом месяце вы получаете прибыль в размере ', pribyl)
elif ubytoc> pribyl:
    print('В этом месяце вы ушли в минус ', ubytoc)

personal=int(input('Введите колличество сотрудников: '))
razn = pribyl//personal
print('прибыль фирмы в расчете на одного сотрудника', razn)

