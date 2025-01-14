# N 입력받기
N = int(input())

# N개의 정수 입력받기 A 배열에 추가될
A = set(map(int,input().split()))
    
# M 입력받기
M = int(input())

# M개의 정수 입력받아서 A 배열에 있으면 1, 없으면 0 출력하기

# 단순히 값 in A 로직으로 풀이가 가능할지?
# => list 사용 시 시간초과됨
# set으로 변환 시 시간 복잡도가 O(N) 에서 O(1) 로 줄어듦
my_list = list(map(int,input().split()))

for ele in my_list:
    if ele in A:
        print(1)
    else:
        print(0)