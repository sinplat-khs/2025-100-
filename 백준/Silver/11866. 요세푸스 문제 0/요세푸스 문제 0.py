# 입력받기
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().strip().split())

# N명의 사람, K번째를 지속해서 지워나감

# 풀이 아이디어
# [1,2,3,4,5,6,7] 이 주어지면 우선 3번째인 3을 제거
# 3을 제거하면서 앞에 있는 1,2는 뒤로 붙여야됨
# 다시 처음부터 3번째인 6을 제거
# ... 반복

my_list = deque(list(range(1,N+1)))
answer = []
while len(my_list) > 0:
    for i in range(K):
        ele = my_list.popleft()
        my_list.append(ele)
        
    answer.append(my_list.pop())
    
print(str(answer).replace('[','<').replace(']','>'))


