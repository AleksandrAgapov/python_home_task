# 20.	Определить, присутствует ли в заданном списке строк, некоторое число 

lst = [2,4,5,8,6,55,577,952,48,8785,951,88,97]
a = (int(input('введите искомое число =   ')))
for i in lst:
    if a == i:
        print('число найдено в этом списке')
        break
    else:
        continue
    