vet_a = []
vet_b = []
vet_c = []

for i, number in enumerate(range(10), start=1):
    vet_a.append(int(input(f'{i}º número do vetor A: ')))
    vet_b.append(int(input(f'{i}º número do vetor B: ')))


for x, y in zip(vet_a, vet_b):
    vet_c.append(x)
    vet_c.append(y)

print(vet_c)