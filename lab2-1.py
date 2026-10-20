# age  = int(input('Введите возраст: '))
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')
########################

# parol = input('Введите пароль: ')
# word = 'secret123'
# if parol == word:
#     print('Вход успешный')
#
# else:
#     print('Неверный пароль')

########################

# price = float(input('Введите сумму: '))
#
# if price > 5000:
#     sale = price* 0.90
#     print(f'Стоимость со скидкой 10%: {sale} сом')
# else:
#     print(f'Исходная стоимость: {price:.2f} сом.')

########### ############

x = float(input("Введите координату X (не 0): "))
y = float(input("Введите координату Y (не 0): "))

if x > 0 and y > 0:
    quarter = "I"
elif x < 0 and y > 0:
    quarter = "II"
elif x < 0 and y < 0:
    quarter = "III"
elif x > 0 and y < 0:
    quarter = "IV"
else:
    quarter = "не определена (одна из координат равна 0)"

print(f"Точка находится в {quarter} координатной четверти.")
#
# ############ ############
#
# osenka = int(input('Введите оценку: '))
# if osenka > 90:
#     print('Отлично (5)')
# elif osenka > 89:
#     print('Хорошо (4)')
# elif osenka > 74:
#     print('Удовлетворительно (3)')
# elif osenka > 50:
#     print('Неудовлетворительно (2)')
