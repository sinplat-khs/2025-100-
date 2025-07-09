# 입력받기

N = int(input())

# 풀이 아이디어
# 2*(N-1) 줄 까지 별을 출력하기
# 출력하는 별 갯수는 
# 현재 반복 수 <= N 인 경우 최초 1에서 2씩 더하기
# 그 이외의 경우 현재 값 - 2 를 해서 출력하기
num = 1
for i in range(2*N-1):
    blank_num = (2*N - num) //2
    
    print(' '*blank_num,'*'*num, sep ='')
    
    if i < N-1:
        num +=2
    else:
        num -= 2