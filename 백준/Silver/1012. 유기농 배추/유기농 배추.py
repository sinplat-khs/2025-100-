from collections import deque
import sys

input = sys.stdin.readline # 빠른 입력 처리


# 방향에 대해 미리 선언해두기 순서 = 상,하,좌,우
dx = [0,0,-1,1]
dy = [-1,1,0,0]


# visited를 바꿔주는 함수
def visiting(x, y, field, visited, M, N):
    queue = deque()
    queue.append((x,y)) # 방문한 좌표 queue에 추가
    visited[y][x] = True
    
    while queue: # 방문한 좌표에 대해 체크
        cx, cy = queue.popleft() # 가운데 좌표, 가운데에서 좌우양옆을 확인
        for direction in range(4):
            nx = cx + dx[direction]
            ny = cy + dy[direction]
            
            if 0 <= nx < M and 0 <= ny < N: # 배추밭 배열 내에 존재하는 좌표인지 확인
                if field[ny][nx] == 1 and not visited[ny][nx]: # 해당 좌표를 확인했는지 여부
                    visited[ny][nx] = True
                    queue.append((nx,ny)) # 해당 좌표랑 이어져있으면 visited를 True로 켜서 다시는 안들르게



# 배열 중에 연결된 그룹이 몇 개인지 판단하기

# 입력받기

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 가로 x 세로 , 배추의 개수
    
    
    # 배추밭 선언
    field = [[0]*M for _ in range(N)]
    
    # 방문 여부를 bool list로 저장
    visited = [[False]*M for _ in range(N)]
    
    # 배추 위치 표시하기
    for _ in range(K):
        x, y = map(int, input().split())
        # x좌표, y좌표
        field[y][x] = 1
        
    # 지렁이 개수
    worm_count = 0
    # 배추밭을 탐색하며 확인
    for y in range(N):
        for x in range(M):
            
            if field[y][x] == 1 and not visited[y][x]:
                visiting(x,y,field,visited,M,N)
                worm_count += 1
                
    print(worm_count)