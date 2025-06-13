import sys

# 속도 개선을 위해 재선언
input = sys.stdin.readline
print = sys.stdout.write
# 아이디어
# 모든 리스트를 저장할 시 메모리 에러 발생
# 수의 범위를 list로 저장해두고 해당 수가 들어오면 count만 올리기

# 첫 수는 갯수
N = int(input())
count = [0] * 10001 #

for _ in range(N):
    count[int(input())] += 1
    
    
for num in range(10001):
    for _ in range(count[num]):
        print(f"{num}\n")