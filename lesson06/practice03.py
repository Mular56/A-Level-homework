#Візьміть файл, в якому є багато англійських слів у рядках. Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.

word_frequency = {}
with open('lesson06\practice03.txt', "r") as filename:
    content = filename.read()
    
words = content.split()

word_frequency = {}
for word in words:
    word = word.strip('.,!?')   #Видаляємо знаки пунктуації
    word = word.lower()   #нижній регістр
    word_frequency[word] = word_frequency.get(word, 0) + 1

sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)  #отримуємо ключ-значення, сортуємо ключі за 2 значення (за частотою), в порядку зменшення

for word, frequency in sorted_word_frequency:
    print(f"{word}: {frequency} times")