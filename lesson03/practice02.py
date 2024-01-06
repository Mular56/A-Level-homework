# 2. Написати програму, яка виводить сама себе

filename = 'lesson03\practice02.txt'

f = open(filename, 'r') 

for line in f: 
    print(line)

f.close()
