3.#	Вывести на экран числа от -N до N

n =int(input( 'Введите  число'   ))
#b =int(input( 'Введите положительное  число'   ))
if n==0:
    (print('введенное нулевое число'))
else:
    for i in range(-n,n+1):
        print(i)

