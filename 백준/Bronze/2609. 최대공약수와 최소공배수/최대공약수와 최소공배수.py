# 두 수 입력받기

a, b = map(int,input().split())


# 일반적인 계산

# 최대공약수
# 1부터 a와 b를 나눈 나머지가 0인 최대값 구하기 a,b중 작은 값까지
max_num = 1
for i in range(1, min(a,b)+1):
    if (a%i == 0) and (b%i == 0):
        max_num = i

print(max_num)

# 최소공배수
# 두 수를 곱해서 최대공약수로 나누기
min_num = (a*b)/max_num
print(int(min_num))