'''

Выведите таблицу размером n×nn×n, заполненную числами от 11 до n2n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

'''


# put your python code here
n = int(input())

k = 0
a = [[0 for i in range(n)] for j in range(n)]
c = 1
i = 0
for k in range(0, n):
    for j in range(k, n - k):  # verhnyaya gorizontal'
        a[i][j] = c
        c += 1
    k += 1  # j = n-k-1
    for i in range(k, n - k + 1):
        a[i][j] = c
        c += 1  # i = n-k
    for j in range(n - k - 1, k - 2, -1):
        a[i][j] = c
        c += 1  # j = k-1
    for i in range(n - k - 1, k - 1, -1):
        a[i][j] = c
        c += 1  # i = k
    if c == n ** 2 + 1:
        break

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()