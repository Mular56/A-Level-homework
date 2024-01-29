#Другий рівень ("if-elif-else"): Придумати власні приклади на альтернативні варіанти if і активне використання булевої алгебри.

#Створіть систему оцінювання для студентів. Запитайте користувача про його бали та використовуйте if-elif-else для призначення оцінок на основі заданих критеріїв.

rating = int(input("Enter your rating: "))

while rating <= 100:
    if rating >= 85:
        print("Your mark is 5! Good gob!")
        break
    elif rating >= 75:
        print("Your mark is 4! Well done!")
        break
    elif rating >= 60:
        print("Your mark is 3!")
        break
    else:
        print("You are not certified.")
        break
else:
    print("Eror! Try one more time.")
    
    
#Задано рік та місяць. Розробити програму, яка визначає:
#чи заданий рік високосним;
#кількість днів у заданому місяці цього року.

year = int(input("Enter year: "))

if not year % 4:
    print("This is leap year!")
else:
    print("This is not leap year!")
    
month = int(input("Enter month (1-12): "))

if month == 2 and not year % 4:
    print("There is 29 days in this month!")
elif month == 2 and year % 4:
    print("There is 28 days in this month!")
elif month % 2:
    print("There is 31 days in this month!")
else:
    print("There is 30 days in this month!")