#Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. Читайте із файлу перший рядок з трьома числами, беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.

filename = 'lesson03\modern fizz-buzz.txt'
f = open(filename, 'r') 

for line in f: 
    fizz = int(line[0])
    buzz = int(line[2])
    third = int(line[3:-1])
    number = 1
    
    while number <= third:
        if not number % fizz and not number % buzz:
            print("FB", end =' ')
            number += 1
        elif not number % buzz:
            print("B", end =' ')
            number += 1
        elif not number % fizz:
            print("F", end =' ')
            number += 1
        else:
            print(number, end =' ')
            number += 1
    print("\n")

f.close()                      #ЧОМУСЬ НЕПРАВИЛЬНО ВИВОДИТЬ ОСТАННЮ ТРІЙКУ ЧИСЕЛ...