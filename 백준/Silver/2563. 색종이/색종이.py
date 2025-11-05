# 색종이의 수 입력받기

N = int(input())

# 배열로 색종이 위치 저장해두기
my_tensor = []

for i in range(N):
    my_list = list(map(int, input().split()))
    
    my_tensor.append(my_list)
    
    
# [0] 최대값 +10 , [1] 최대값 +10 크기의 배열 생성해두기
max_row = max(list(x[0] for x in my_tensor))
max_col = max(list(x[1] for x in my_tensor))

my_tensor2 = [[0]*(max_col+10) for _ in range(max_row+10)]


# x,y 좌표에 1을 채우기

for x,y in my_tensor:
    # x좌표 시작점부터 +10까지
    for i in range(x,x+10):
        for j in range(y,y+10):
            my_tensor2[i][j] = 1
            
            
# 1로 채워진 면적 계산하기 (중복은 알아서 1로 고정돼있음)

print(sum(sum(row) for row in my_tensor2))

