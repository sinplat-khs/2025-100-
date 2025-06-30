# 입력받기
N, M = map(int, input().split())


# 풀이 아이디어
# N = 바구니 갯수
# M = 시행 횟수
# 바구니 인덱스를 방문하면서 k로 교체하기
my_list = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for ele in range(i,j+1):
        my_list[ele-1] = k
        
for ele in my_list:
    print(ele, end = ' ')
    
    