# 입력값 받기
import sys

N, K = map(int,sys.stdin.readline().strip().split())

# 이항계수 = N부터 N-1 , N-2 곱하기 .. (K번)
# 분모를 1 2 3 4 ... 곱하기 (K번)


# k번 반복하기
son_num = N
mom_num = 1
target_num = 1
for _ in range(K):
    # 분자 = ?
    target_num = (target_num * son_num) / (mom_num)
    son_num -= 1
    mom_num += 1
    
print(int(target_num))
    
    
    