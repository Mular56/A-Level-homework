#Цифры до точки с запятой надо суммировать, потом делить на их количество. В первой строке сумма будет 11, разделить на их количество, т.е. на 3, получается 3 целых и в остатке 2. Аналогичным образом во второй строке 6 делим на три, ровно два и в остатке ноль, в третьей строке сумма 16, на 5 делим, получаем 3 и 1 в остатке. Вот так:
#Задача: проверить каждую строку файла, если строка записана верно, вывести ее и после написать True, если строка не верна, вывести результат с пометкой False.

with open('lesson04/practice03.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        line_1 = line.split(";")[0]  # до ;
        line_2 = line.split(";")[1]  # після ;
        current_sum = 0
        count = 0
        for n in line_1:
                if n.isdigit():   #перевіряє чи це числа
                    current_sum += int(n)  # сумма
                    count += 1  # кількість чисел
                check_number = []
                for n in line_2:
                    if n.isdigit():
                        check_number.append(int(n))   #числа для перевірки
                
        check = False if current_sum // count == check_number[0] and current_sum % count == check_number[1] else True
        print(f'{line} - {check}')
        
