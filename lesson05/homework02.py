#Створити структуру даних для студентів з імен та прізвищ, можна випадкових. Придумати структуру даних, щоб вказувати, у якій групі навчається студент (Групи Python, FrontEnd, FullStack, Java). Студент може навчатися у кількох групах. Потім вивести:
#- студентів, які навчаються у двох та більше групах
#- студентів, які не навчаються на фронтенді
#- студентів, які вивчають Python або Java
 
student_data = {
    'John Smith': ['Python', 'FrontEnd', 'Java'],
    'Alice Johnson': ['FullStack'],
    'Bob Williams': ['FrontEnd', 'FullStack'],
    'Emma Jones': ['Python', 'Java'],
    'David Brown': ['FrontEnd', 'FullStack', 'Java'],
    'Olivia Davis': ['Python'],
    'Charlie Miller': ['Python', 'FrontEnd', 'Java'],
    }

print("Students studying in two or more groups: ")
for student, group in student_data.items():
    if len(group) >= 2:
        print(f"{student}: {', '.join(group)}")

print("\nStudents is not studying in FrontEnd: ")
for student, group in student_data.items():
    if 'FrontEnd' not in group:
        print(f"{student}: {', '.join(group)}")
        
print("\nStudents studying in Python or Java: ")
for student, group in student_data.items():
    if 'Python' or 'Java' in group:
        print(f"{student}: {', '.join(group)}")
        
