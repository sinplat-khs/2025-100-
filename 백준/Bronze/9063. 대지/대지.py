# 테스트 케이스 입력받기
N  = int(input())

my_list = []
# 리스트로 저장
for _ in range(N):
    x, y = map(int,input().split())
    my_list.append([x,y])
    
# [0]번째 인덱스 중에서 최대, 최소
# [1]번째 인덱스 중에서 최대, 최소 

x_list = [x for x, y in my_list]
y_list = [y for x, y in my_list]

max_x = max(x_list)
min_x = min(x_list)

max_y = max(y_list)
min_y = min(y_list)

# 넓이
answer = (max_x - min_x)*(max_y - min_y)

print(answer)