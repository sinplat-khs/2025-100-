import sys

# 풀이 아이디어

# 전체 칸을 4분면으로 나눔
# -> 속한 곳을 확인 해서 칸 수를 더함 (방문 횟수를 추가하는 것)
# -> 속한 곳에서 4분면으로 또 나눔
# 한 변의 길이가 2일 때까지 반복하기

def search(n, r, c):
    answer = 0
    while n > 0:
        half = 1*(2**(n-1)) # 변의 길이 절반
        # 속한 영역을 확인하기 0, 1, 2, 3
        # 행*2
        # 열*1
        if r >= half:
            r_area = 1
        else:
            r_area = 0
            
        if c >=half:
            c_area = 1
        else:
            c_area = 0
        area = r_area*2 + c_area
        
        # 정답에 4분면으로 나뉜 칸 수 더하기
        answer += area*(half*half)
        
        # 행열을 4분면 칸수 만큼 빼기 (전진했다고 생각)
        r %= half
        c %= half 
        n -= 1
    return answer

N, r, c = map(int, sys.stdin.readline().split())
print(search(N,r,c))