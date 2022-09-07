list_averages = []

average = 0

for n in range(3):
    for i, j in enumerate(range(4), start=1):
        student_grade = float(input(f'{i}º nota : '))
        average += student_grade

    print('*=' * 6)
    average = average / 4
    list_averages.append(average)
    average = 0

filtered_averages = list(filter(lambda x: x >= 7, list_averages))

print(f'\n{len(filtered_averages)} alunos tem a média maior ou igual a 7.')