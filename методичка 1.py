#ВЕТВЛЕНИЯ
number = 157
if not number % 2: #остаток от деления на 2 равен 1, что эквивалентно true.
    print('число четное')
else:
    print('число не четное')

#СПИСКИ

half_year_months = ['январь', 'февраль', 'март', 'апрель', 'июнь']
print(type(half_year_months))
print(half_year_months[2]) # март
half_year_months[2] = 'fff'
print(half_year_months[2]) # fff
half_year_months.append('в конец')# добавление в конец списка
print(half_year_months)#

#ЦИКЛЫ
len()