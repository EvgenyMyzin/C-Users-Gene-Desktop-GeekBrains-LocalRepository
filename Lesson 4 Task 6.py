"""Homework 4 Task 6

    6. Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. 
    Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
    Необходимо предусмотреть условие его завершения.
    Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
    Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
    """


from itertools import count
from itertools import cycle

a=[el for el in range( 2, 11 ) if el%2==1]
print(a)

for el in count( 7 ):
    if el > 15 :
        break
    else :
        print(el)

c = 3
for el in cycle(a):
    if c > 10 :
        break
    print(el)
    c += 1


