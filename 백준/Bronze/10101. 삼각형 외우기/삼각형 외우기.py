# 3줄 입력받기

my_list = []
for _ in range(3):
    angle = float(input())
    
    my_list.append(angle)

A, B, C = my_list


if (A==60) and (B==60) and (C==60):
    print('Equilateral')
    
elif (A+B+C) == 180:
    if (A==B) or (B==C) or (C==A):
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')