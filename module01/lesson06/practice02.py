#Написати функцію, яка буде підносити число у квадрат. Написати другу, яка буде перевіряти, чи є число простим. Потрібно видрукувати в головній програмі квадрати усіх простих чисел зі списку від 0 до 50 за допомогою map

def squared_number (x):
    return x ** 2

def prime_number (n):
    if n < 2:
        return False   #щоб не виводило 0, 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
numbers = list(range(51))
checking = list(map(squared_number, filter(prime_number, numbers)))

print(numbers)
print(checking)