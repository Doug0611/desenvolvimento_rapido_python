numbers = []

for i, number in enumerate(range(10), start=1):
    numbers.append(float(input(f'{i}º número inteiro: ')))

sum_of_squares = sum([x**2 for x in numbers])

print(sum_of_squares)