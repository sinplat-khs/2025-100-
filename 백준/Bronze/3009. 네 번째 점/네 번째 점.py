# 요소 세기를 위한 collections Counter
from collections import Counter

# 3 점의 좌표 입력 받기
my_list = []

for _ in range(3):
    x, y = map(int, input().split())
    my_list.append([x,y])
    
# 3점의 좌표가 저장돼있음

# 축에 평행한 직사각형 = 2점의 x좌표가 같음, 2점의  y좌표가 같음
# [0] 번째 인덱스에서 1번 등장한 거 찾기
# [1] 번째 인덱스에서 1번 등장한 거 찾기
x_list = [x for x ,y in my_list]
y_list = [y for x, y in my_list]

# x_list, y_list에서 각 요소가 등장한 횟수 저장
x_counter = Counter(x_list)
y_counter = Counter(y_list)

answer_x = [x for x, count in x_counter.items() if count == 1][0]
answer_y = [y for y, count in y_counter.items() if count == 1][0]

print(answer_x, answer_y)
    
    
    
