#Было
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#number = int(input())
#mult = 1
#list = []
#for i in range(1, number+1):
    #mult*=i
    #list.append(mult)
#print(list)

#Стало
from math import factorial
number = int(input())
list = [ factorial(i) for i in range(1, number+1) ]
print(list)