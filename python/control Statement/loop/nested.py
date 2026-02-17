#aloop under loop ko nested loop khete hai

for i in range(1, 3):




    for j in range(3, 6):
        print(f'{i}, {j}')

#nested list list ke andar list ko nested list kehte hai

a = [1, 2, 3, 4, 5]
b = [6, 7, a, [7, 8, 9]]
print(b)