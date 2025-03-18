# 입력받기
import math # 올림 계산을 위함
import sys

N = int(sys.stdin.readline().strip())

S, M, L, XL, XXL, XXXL = map(int, sys.stdin.readline().strip().split())

T, P = map(int, sys.stdin.readline().strip().split())

# 풀이 아이디어
# S, M ... 을 T로 나눈 몫을 모두 더함 답1
# N을 P로 나눈 몫과 나머지 출력 답2


print(math.ceil(S/T) + math.ceil(M/T) + math.ceil(L/T) 
      + math.ceil(XL/T) + math.ceil(XXL/T) +  math.ceil(XXXL/T))

print(N//P, N%P)
