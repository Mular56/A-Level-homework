#Перевірити, чи є введене число парним.
number_1 = int(input("Enter a number: "))
if number_1 % 2:
    print("Number is odd")  #непарне
else:
    print("Number is even") #парне


#Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10.
number_2 = int(input("Enter a number: "))
if number_2 % 2 and not number_2 % 15:
    print("number")


#Ввести число, вивести усі його дільники.
number_3 = int(input("Your number = "))
divisor = 1
print("It divisors: ")

while divisor <= number_3:
    if number_3 % divisor == 0:
        print(divisor)
        divisor += 1
    else:
        divisor += 1

    

#Ввести число, вивести його розряди та їх множники.
# discharges - розряди, multipliers - множники

number_4 = int(input("Enter your number: "))
power = 0
x = 10
while number_4 >= x:
    print("discharge = 10^", (power))
    power += 1
    x **= power

reversed_number = 0
while number_4 > 0:
    print("multiplier =", str(number_4)[-1])
    number_4 //= 10  