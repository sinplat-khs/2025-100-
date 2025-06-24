from collections import deque

# 입력 받기
n, m, v = map(int, input().split())

# 그래프 노드 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    # 각 노드에서 갈 수 있는 지점을 표시한다고 생각
    graph[x].append(y)
    graph[y].append(x)
    
#### 오답 수정 ####
# 정점 번호가 작은 것부터 처리하는 조건 추가
for i in range(len(graph)):
    graph[i].sort()

# 방문 여부
visited1 = [False] * (n+1)
visited2 = visited1.copy()

# DFS => 깊이 우선 탐색
# 시작 노드에서부터 자식 노드를 순서대로 탐색하는 것
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ') # 줄 바꿈 없애기 => 기본값 end ='\n'
    
    # 현재 노드에서 연결된 인접 노드 체크
    for i in graph[v]:
        if not visited[i]:
            # 해당 노드에서 탐색 실행
            # 탐색을 들어간 노드에서 또 노드가 있다면 거기서 또 시행
            # => 깊이 우선 탐색의 정의, 깊이 끝까지 들어갔다가 상위 노드 체크
            dfs(graph, i, visited)
            
# BFS => 너비 우선 탐색
# 깊이를 체크해서 가장 얕은 부분부터 탐색해나가기
def bfs(grpah, v, visited):
    # 시작 노드를 Q에 넣고 시작
    queue = deque([v])
    visited[v] = True
    
    while queue:
        # 선입선출, 첫 수행엔 첫 노드 수행
        v = queue.popleft()
        print(v, end =' ') # 출력 => 줄바꿈 없이
        
        # 인접 노드 확인
        for i in graph[v]:
            if not visited[i]:
                # 인접 노드 체크 세션 추가
                queue.append(i)
                visited[i] = True

                
dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
               