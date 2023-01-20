#Было
#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
#второй и предпоследний и т.д.Пример:- [2, 3, 4, 5, 6] => [12, 15, 16];   - [2, 3, 5, 6] => [12, 15]

# lenght = int(input("введите длину списка: "))
# list = []
# list2 = []
# lenght_list2 = 0
# for i in range(lenght):
#     list.append(int(input("Введите число: ")))
# if lenght % 2 == 0:
#     lenght_list2 = lenght//2
# else:
#     lenght_list2 = lenght//2+1
# for i in range(lenght_list2):
#     list2.append(list[i]*list[-1-i])
# print(list2)

#Стало

list_1 = [int(i) for i in input('Введите значения через пробел: ').split()]
lenght = int(len(list_1)/2)
if len(list_1) % 2 == 1:
    lenght+=1
list_2 = [ list_1[i]*list_1[-1-i] for i in range(0, lenght)]
print(list_2)
