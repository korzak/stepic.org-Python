'''

Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3

'''

with open("1.txt","r") as inp:
    arch=inp.read().lower().split()
distinct=set(i for i in arch)
max_count=0
for i in range(len(arch)):
    if arch.count(arch[i])>max_count:
        max_count=arch.count(arch[i])
for k in distinct:
    if arch.count(k)==max_count:
        print(k,arch.count(k))