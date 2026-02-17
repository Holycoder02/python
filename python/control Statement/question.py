"""
1-10
even number
2,4,6,8,10

odd number
1,3,5,7,9

%2 == 0 even number

2 % 4 = 0

i = 1
i = 2
i = 3...
i = 10
"""

for i in range(1,100):
    if i % 2 == 0:
        print(f'{i} is even number')
    else:
        print(f'{i} is odd number')