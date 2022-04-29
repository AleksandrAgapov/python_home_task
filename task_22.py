#22.	Найти сумму чисел списка стоящих на нечетной позиции
my_spisok = [1,3,4,6,7,5,9,11,7,44]
sum=0
for i in range(len(my_spisok)):
    if i % 2 == 1:
        sum+=my_spisok[i]
print (sum)
       

