# 조건 입력받기
N= int(input())
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))

############ 풀이 아이디어 ##########
# 곱셉 계산의 경우, 큰 값끼리 곱하는 경우를 피해야함
# A를 내림차순 정렬, B를 오름차순 정렬해서 순서대로 곱하기
####################################


A.sort()
B.sort(reverse=True)
value = 0

for i in range(len(A)):
    value += A[i]*B[i]
    
print(value)