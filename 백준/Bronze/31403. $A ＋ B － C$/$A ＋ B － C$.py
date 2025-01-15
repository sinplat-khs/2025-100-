# A, B, C를 차례대로 입력받기
A = int(input())
B = int(input())
C = int(input())

# 숫자로 생각한 경우

print(A+B-C)

# 문자열로 생각하는 경우

# A + B를 먼저 연산
temp1 = str(A)+str(B)

# str로 연산된 값을 int로 변환
temp2 = int(temp1)

# 마지막으로 -C 연산

print(temp2 - C)