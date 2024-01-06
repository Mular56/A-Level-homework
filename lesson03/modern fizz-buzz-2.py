#Переробити другу задачу так, щоб результат писався в інший файл. Додаємо list comprehension, map та інші свіжеотримані знання до виконання завдання.

with open('lesson03\modern fizz-buzz.txt', "r") as file1:
    with open('lesson03\ new file.txt', "w") as file2:
        for line in file1: 
            fizz = int(line[0])
            buzz = int(line[2])
            third = int(line[3:-1])
            
            for number in range(1, third):
                if not number % fizz and not number % buzz:
                    file2.write(str("FB "))
                    number += 1
                elif not number % buzz:
                    file2.write(str("B "))
                    number += 1
                elif not number % fizz:
                    file2.write(str("F "))
                    number += 1
                else:
                    file2.write(str(number) + " ")
                    number += 1
            file2.write("\n")