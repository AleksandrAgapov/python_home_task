#12.	Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.Для n = 6: 
# {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

from msvcrt import kbhit


def New_Dict(n):
    k=0
    v=0
    dict={}
    while len(dict) !=n:
        k+=1
        #v = 3*k + 1
        dict[k] = v

    return dict

a = int(input('Введите количество членов словаря '))
print(f'Словарь: {New_Dict(a)}')