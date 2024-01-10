# Написати 2 функції. Перша функція прийматиме рядок та приводитиме його до нижнього регістру. Друга функція прийматиме рядок та приводитиме його до верхнього регістру.
#  Головна програма має застосовувати обидві функції до списку рядків за допомогою `map`, для кожного з рядків, та друкувати результат.

text_input = str(input("Enter your text: "))
text = text_input.split()

def function_1(word):
    return word.lower()

def function_2(word):
    return word.upper()

result_1 = list(map(function_1, text))
result_1_string = ' '.join(result_1)
result_2 = list(map(function_2, text))
result_2_string = ' '.join(result_2)

print(result_1_string, "\n", result_2_string)

#We can share THIS text - test