# 입력받기

import sys

N = int(sys.stdin.readline().strip())

# N개의 입력값 받기

my_list = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    
    # x좌표에 대한 오름차순, 그 이후 y좌표에 대한 오름차순으로 정렬하기
    # list.sort(key=lambda x : func(x)) 로 오름차순 규칙 설정하기
     
    # 1. list로 만들기
    my_list.append([x,y])
    
# 2. x값에 대해 오름차순 정렬
# ele의 0번째, 즉 x값에 대한 정렬
# my_list.sort(key = lambda ele : ele[0])

# 3. x값이 같은 경우에는 y값 오름차순으로 정렬하기?
my_list.sort(key = lambda ele : (ele[0], ele[1]))



for ele in my_list:
    print(ele[0], ele[1])
    