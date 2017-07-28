'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где 
mod — это взятие остатка от деления, 
pow — возведение в степень, 
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.

Sample Input 1:
5.0
0.0
mod
Sample Output 1:
Деление на 0!

'''

# put your python code here
#+, -, /, *, mod, pow, div,
st=float(input())
nd=float(input())
oper=str(input())

if nd==0 and (oper=='/' or oper=='mod' or oper=='div'):
    print("Деление на 0!")
else:
	if oper=='/':
		print( st / nd )
	elif oper=='mod':
		print( st % nd )
	elif oper=='pow':
		print( st ** nd )
	elif oper=='+':
		print( st + nd )
	elif oper=='-':
		print( st - nd )
	elif oper=='*':
		print( st * nd )
	elif oper =='div':
		print( st // nd )
