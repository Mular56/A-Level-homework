#Створити словник оцінок передбачуваних студентів (Ключ – ПІ студента, значення – список оцінок студентів). Знайти найуспішнішого і самого слабенького за середнім балом.
    

assessments = {
    "Smith": [83, 60, 65],
    "Johnson": [68, 96, 81], 
    "Williams": [86, 67, 65], 
    "Brown": [73, 89, 71], 
    "Miller": [96, 79, 83]
}
print(f"{assessments}: ")

def calculate_average_score(scores):
    return sum(scores) / len(scores)

highest_score = 0
lowest_score = float('inf')
most_successful_student = ''
weakest_student = ''

for student, scores in assessments.items():
    average = calculate_average_score(scores)
    if average > highest_score:
        highest_score = average
        most_successful_student = student
    if average < lowest_score:
        lowest_score = average
        weakest_student = student

print("Most successful student: ", most_successful_student, "with an average score of ", highest_score)
print("Weakest student: ", weakest_student, "with an average score of ", lowest_score)
