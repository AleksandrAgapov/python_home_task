#5.	Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

a =int(input( 'Введите  число   '   ))
if a % 5 == 0:
 print('число a кратно   5 ')
else:
    print('число a не кратно   5  ') 
if a % 10 == 0:
   print('число a кратно    10 ') 
else:
    print('число a не кратно    10 ') 
if a % 15 ==0:  
   print('число a кратно   15  ') 
else:
    print('число a не кратно не  15  ') 
