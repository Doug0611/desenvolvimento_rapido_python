student_grades = []

average = lambda x: sum(x) / len(x)

for i, grades in enumerate(range(4), start=1):
    student_grades.append(float(input(f'{i}º nota: ')))

print()
print(f'suas notas: {student_grades}.')
print(f'sua média: {average(student_grades)}')

