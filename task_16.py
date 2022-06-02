	#Задать список из n чисел последовательности (1+(1/n))^n и вывести на экран их сумму

    
def multi(a):
  i=1
  sum=0
  num=1
  list =[]
  while i<=a:
     num=(1+(1/num))**num
     list.append(num)
     i=i+1
  for i in list:
      sum=sum+i
     
  return sum

a=int(input(' введите число  '))
print(f'сумма списка из n последовательности равна  : {multi(a)}')


