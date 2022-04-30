# 24.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением 
# дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

def nums (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(mynums):
    nums = [round(x - int(x), 2) for x in (mynums)]
    return max(nums) - min(nums)

n = 5
frst = 1
last = 10
mynums = nums(n, frst, last)

print (mynums)
print(find_diff(mynums))