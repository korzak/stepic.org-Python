'''

Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

Sample Input 1:
5
-3
8
4
0
Sample Output 1:
14

'''

# put your python code here
n = int
sum1 = 0
i = int
while i != 0:
    n = int(input())
    sum1 = sum1 + n
    i = n

print(sum1)