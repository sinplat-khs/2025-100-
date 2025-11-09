# 양쪽 중 큰 지점 A, 적은지점 B 라고 가정
# A 개의  지점 중에서 B개의 지점을 선택해서 다리를 놓는 경우이므로
# A C(콤비네이션) B
# = factorial(A) / factorial(A-B)


# factorial 함수 선언
def factorial(n):
    for i in range(n-1):
        n *= i+1
    return int(n)
        
# 계산
X = int(input())
for i in range(X):
    r,c = map(int,input().split())
    if r>c:
        print(int(factorial(r)/(factorial(c)*factorial(r-c))))
    elif r<c:
        print(int(factorial(c)/(factorial(r)*factorial(c-r))))
    else:
        print(1)
        
        