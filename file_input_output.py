'''

Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667

'''

with open('dataset_3363_4.txt', 'r') as inf:
    s = [line.strip().split(';') for line in inf]

i1_sum, i2_sum, i3_sum = 0, 0, 0
for i in s:
    print((int(i[1]) + int(i[2]) + int(i[3])) / 3)
    i1_sum, i2_sum, i3_sum = i1_sum + int(i[1]), i2_sum + int(i[2]), i3_sum + int(i[3])
print(i1_sum / len(s), i2_sum / len(s), i3_sum / len(s))


'''
with open('dataset_3363_4.txt','r') as ifile, \
        open('output.txt','w') as ofile:
    average,counter = [],0
    for line in ifile:
        marks = [int(i) for i in line.strip().split(';')[1:]]    
        counter += 1
        if not len(average):
            average = [0]*len(marks)    
        for i in range(len(marks)):
            average[i] += marks[i]  
        ofile.write(str(sum(marks) / len(marks)) + '\n')
    ofile.write(' '.join(str(mark/counter) for mark in average))
'''