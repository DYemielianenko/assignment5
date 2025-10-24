import csv

all_students = []
with open('dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        all_students.append(row)

for student in all_students:
    s = 0
    for key in student:
        if key in ['Основи програмування', 'Лінійна алгебра', 'Проекційна геометрія', 'Математичний аналіз']:
            s += int(student[key])
    student["Середня оцінка"] = s/4

request = input("Введіть назву однієї групи для експорту: ")
while request not in set(all_students[i]['Група'] for i in range(len(all_students))):
    request = input("Введіть дійсну назву групи для експорту: ")

fieldnames = ['Id', 'Прізвище', 'Ім\'я', 'Група',
              'Основи програмування', 'Лінійна алгебра',
              'Проекційна геометрія', 'Математичний аналіз',
              'Середня оцінка']

with open(f"{request}.txt", mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for student in all_students:
        if student["Група"] == request:
            writer.writerow(student)

print(f"Завершено. Створено файл {request}.")