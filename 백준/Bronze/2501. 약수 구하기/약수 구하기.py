# N, K 입력받기

N, K = map(int, input().split())

# 1부터 N까지 시작해서 N을 나눌 수 있는 숫자 찾기
# K번째가 되면 끝내기

count = 0
for i in range(1, N+1):
    
    if N%i == 0:
        count += 1
        
        if count == K:
            print(i)
            break
            
# for문이 break 없이 끝난 경우에만 실행됨 ☆
else:            
    print(0)