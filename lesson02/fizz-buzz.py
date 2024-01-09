#Ви маєте три числа, вони вводяться з консолі. Перше число називається fizz, друге називається buzz. До третього необхідно дорахувати від одиниці. Дивлячись на поточне число, якщо воно кратне fizz – треба виводити F замість числа. Якщо число кратне buzz – треба виводити B замість числа. Якщо число кратне і fizz, і buzz, треба виводити FB. Якщо воно не кратне нічому, виводимо число. І так - поки не буде досягнуто третього введеного числа.

#Приклад умови та результату: Введено числа 2, 5, 18 Висновок має бути таким:

#1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

fizz = int(input("Enter fizz-number: "))
buzz = int(input("Enter buzz-number: "))
third = int(input("Enter third number: "))
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
        
print("\n That`s all))\n")
