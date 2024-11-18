# N 회의의 수 input으로 받기
N = int(input())

# 초기값 선언
end_time = 0 # 현재 시각 (초기 시간은 0, 회의 배정되면 해당 회의 끝나는 시간을 현재로 생각)
time_list= [] # 정렬을 위한 리스트 선언, 이후 start, end 시간 append 예정
count=0 # 정답 제출을 위한 회의 수

# 회의의 수 만큼 start시간, end 시간 받기
for i in range(N):
    start,end = map(int,input().split(' '))
    time_list.append([start,end]) # [[start1, end1], [start2, end2], ... ]
    
# 끝나는 시간으로 정렬
# 1. 현재 기준 가장 일찍 끝나는 회의 진행 (일찍 끝나는 회의 = 남은 시간의 최대값)
# 2. 해당 아이디어의 반복
time_list = sorted(time_list, key = lambda time:(time[1],time[0]))

# 회의 수 만큼 탐색 반복
for i in range(N):
    # 현재 시각 <= i번째 회의의 시작 시간인 경우 (현재 시점에서 가능한 회의 필터링) 
    # 해당 회의 배정, count 1개 up, 현재 시각을 해당 회의 끝나는 시간으로 변경
    if end_time <= time_list[i][0]:
        count+=1
        end_time = time_list[i][1]
    
    # 현재 시각 > i번째 회의의 시작 시간
    # 즉, 현재 시각에서 불가능함 (이미 지나버린 회의시간)
    else:
        continue

# 정답 출력
print(count)