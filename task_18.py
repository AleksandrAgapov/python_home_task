# 18.	Реализовать алгоритм перемешивания списка. 
import random
def range_list(a,b):
 numbert =list(range(a,b))
 return numbert

s=int(input(' введите первое число диапазона  = '))
k=int(input(' введите второе число диапазона  = '))
c=range_list(s,k)
print(f'начальный упорядоченный список',c)
c1=c
random.shuffle(c1)
print(f'перемешанный список',c1)


