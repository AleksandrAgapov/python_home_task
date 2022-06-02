# 15.	Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def multi(a):
  i=1
  sum=1
  list =[]
  while i<=a:
     sum=sum*i
     list.append(sum)
     i=i+1
     
  return list

a=int(input(' введите число  '))
print(f'произведение чисел натурального числа равна : {multi(a)}')

