# N 입력받기
N = int(input())

# 반복하는 동작
# 위에 있는 카드를 제거
# 위에 있는 카드를 맨 밑으로 이동

# list로 1~N개의 카드를 선언하기


# num_list 의 길이가 1이 될 때까지 반복하기
# => 정직하게 반복하니 시간초과됨
# 풀이아이디어: index가 1,3,5,7... 인 것들만 indexing해서 뒤에 붙이기
# 반복


# => list indexing하는데 걸리는 시간복잡도는 해결이 안됨
# => deque로 자료 구조 변경
from collections import deque

num_list = deque(range(1,N+1))

while len(num_list) != 1:
    num_list.popleft()
    num_list.append(num_list.popleft())


        
print(num_list[0])
    