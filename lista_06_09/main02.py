numbers = []

for i, number in enumerate(range(10), start=1):
    numbers.append(float(input(f'{i}° número: ')))

print(sorted(numbers, reverse=True))