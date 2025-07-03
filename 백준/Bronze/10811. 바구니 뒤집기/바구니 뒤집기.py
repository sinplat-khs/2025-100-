# 입력받기
N, M = map(int, input().split())

# N개의 배열 만들기 1,2,3,4,...N
my_list = [x+1 for x in range(N)]

# 풀이 아이디어
# i부터 j까지 반복문으로 값 재정렬하기
# -> i부터 j까지를 리스트로 따로 저장해서 뒤집어놓기

for _ in range(M):
    
    # 입력받기
    i, j = map(int, input().split())
    
    my_list[i-1:j] = my_list[i-1:j][::-1]
    
    
    # rev_list = my_list[i-1:j]
    # rev_list = rev_list[::-1]
    
    # 불필요
    # for index in range(i, j+1):
    #        my_list[index-1] = rev_list[index-1]
        
for ele in my_list:
    print(ele, end=' ')
        