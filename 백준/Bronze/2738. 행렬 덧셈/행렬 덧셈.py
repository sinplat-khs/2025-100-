# 입력받기
N, M = map(int, input().split(' '))


# A, B 선언해두기
# A = []
# B = []

# N개의 줄 만큼 input받아서 A에 append하고, 그다음에 B에 추가
#for _ in range(N):
#    my_list = list(map(int, input().split(' ')))
    
#    A.append(my_list)
    
#for _ in range(N):
#    my_list = list(map(int, input().split(' ')))
    
#    B.append(my_list)
    

# 간단한 풀이 = 미리 NxM 배열을 생성해두고 각위치에 값을 더하기

# NxM 을 0으로 채움
answer = [[0 for x in range(M)] for y in range(N)]

# 입력받으면서 index에 더하기
for i in range(N):
    num_list = list(map(int, input().split(' ')))
    for j in range(M):
        answer[i][j] += num_list[j]
# B의 경우에도 한번 더
for i in range(N):
    num_list = list(map(int, input().split(' ')))
    for j in range(M):
        answer[i][j] += num_list[j]
                    

# 정답 출력하기
for i in range(N):
    print(' '.join(map(str, answer[i])))
    
        

        
        