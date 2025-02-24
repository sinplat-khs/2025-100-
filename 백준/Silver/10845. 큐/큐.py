# 명령 갯수 입력받기
# deque 사용하기
from collections import deque
import sys

N = int(sys.stdin.readline().strip())

my_queue = deque([])
result = []

for _ in range(N):
    comm = sys.stdin.readline().strip()
    
    if 'push' in  comm:
        num = comm.split()[1]
        my_queue.append(num)
        
    elif 'front' in comm:
        if len(my_queue) > 0:
            print(my_queue[0])
        else:
            print(-1)
        
    elif 'back' in comm:
        if len(my_queue) > 0:
            print(my_queue[-1])
        else:
            print(-1)
        
    elif 'size' in comm:
        print(len(my_queue))
    
    elif 'pop' in comm:
        if len(my_queue) > 0:
            num = my_queue.popleft()
            print(num)
        else:
            print(-1)
        
    elif 'empty' in comm:
        if len(my_queue) == 0:
            print(1)
        else:
            print(0)
    