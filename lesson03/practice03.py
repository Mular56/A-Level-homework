#3. Написати програму, яка виводить саму себе задом наперед

filename = 'lesson03\practice03.txt'
filename == str() #???????

f = open(filename.__reversed__, 'r') 

for line in f: 
    print(line)

f.close()