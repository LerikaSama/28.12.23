#Задание 1

#start = int(input("Введите начало диапазона: "))
#end = int(input("Введите конец диапазона: "))

#for a in range(start, end + 1):
#    if a % 7 == 0:
#        print(a)


#Задание 2

#start = int(input("Введите начало диапазона: "))
#end = int(input("Введите конец диапазона: "))

#print("Все числа диапозона:")
#for i in range(start, end+1):
#    print(i, end=" ")
#print()


#print("Все числа диапозона в убывающем порядке:")
#for i in range(end, start -1, -1):
#    print(i, end=" ")
#print()


#print("Все числа, кратные 7:")
#for i in range(start, end+1):
#    if i % 7 == 0:
#      print(i, end=" ")
#print()


#count = 0

#for i in range(start, end+1):
#    if i % 5 == 0:
#        count += 1
#print("Количество чисел, кратных 5:", count)


#Задание 3


start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for i in range(start, end+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)