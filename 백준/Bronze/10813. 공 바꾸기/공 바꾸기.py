# 입력받기
N, M = map(int, input().split())

# N길이의 배열 생성 1,2,3 ... N
my_list = [x+1 for x in range(N)]


# M줄 받기
for _ in range(M):
    i, j = map(int,input().split())
    
    
    # i번째, j번째 index화
    # 미리 기억해두기
    a = my_list[i-1]
    b = my_list[j-1]
    
    # 바꾸기
    my_list[i-1] = b
    my_list[j-1] = a
    
for ele in my_list:
    print(ele,end=' ')