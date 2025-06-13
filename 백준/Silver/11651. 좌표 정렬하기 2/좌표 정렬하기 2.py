import sys

input = sys.stdin.readline

my_list = []

for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    my_list.append((x,y)) # (x1, y1) tuple 형태로 리스트에 넣기
    
# sort key lambda를 사용해서 y를 우선순위로 정렬하기

my_list.sort(key = lambda ele:(ele[1], ele[0]))

for ele in my_list:
    print(ele[0], ele[1])