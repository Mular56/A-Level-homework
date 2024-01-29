def spam(number):
    
    return ''.join(['bulochka' for i in range(number)])

def my_sum(list_of_numbers):
    
    total_sum = 0
    for number in list_of_numbers:
        total_sum += number 
    return total_sum


def shortener(string):
    
    string_split = string.split()
    new_list = []
    for word in string_split:
        if len(word) > 6:
            new_word = word[:6] + '*'
        else:
            new_word = word
        new_list.append(new_word)
    new_string = ' '.join(new_list)
    return new_string


def compare_ends(words):

    words_count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            words_count += 1
    return words_count
