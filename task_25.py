# 25.	Написать программу преобразования десятичного числа в двоичное


n = int(input('Введите число: '))

def conv(n):
    bin_num = ''
    while n > 1:
        bin_num += str(n % 2)
        n = n // 2
    return bin_num[::-1]
print(conv(n))

