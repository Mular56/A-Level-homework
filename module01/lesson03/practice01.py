# 1. Кожен пише суму списку за допомогою for та while

user_list = input("Enter numbers separated by spaces: ")
total_sum = 0

numbers = [int(x) for x in user_list.split()] # метод split() для розділення введених чисел
print(numbers)

for number in numbers:
    total_sum += number
    
print("Total sum = ", total_sum)