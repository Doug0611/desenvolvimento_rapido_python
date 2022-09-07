from functools import reduce


numbers = []

for i, v in enumerate(range(5), start=1):
    numbers.append(int(input(f'{i} ºnúmero: ')))

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
multiplication_of_numbers = reduce(lambda x, y: x * y, numbers)

print(f'\nsoma dos números: {sum_of_numbers}')
print(f'multiplicação dos números: {multiplication_of_numbers}')
print(f'os números digitados foram: {sorted(numbers)}')