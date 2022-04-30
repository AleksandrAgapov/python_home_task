# 23.	Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний 
from random import randint
import math
def numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def pary(mylist):
    return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

n = 10
frst = 1
last = 20

mylist = numbers(n, frst, last)
print(mylist)
print(pary(mylist))








