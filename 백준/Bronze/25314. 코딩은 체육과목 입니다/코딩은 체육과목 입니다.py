# 입력받기
N = int(input())


# 풀이 아이디어
# 입력받은 값을 4로 나눈 만큼 long을 출력 후 + int 출력

n = N//4

for i in range(n):
    print('long',end = ' ')

print('int')