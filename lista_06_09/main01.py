numbers = []

for i, number in enumerate(range(5), start=1):
    numbers.append(int(input(f'{i}° número: ')))

print(numbers)