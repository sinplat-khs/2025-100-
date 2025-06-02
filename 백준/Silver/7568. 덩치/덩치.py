N = int(input())

my_list = []
for _ in range(N):
    x, y = map(int, input().split(' '))
    my_list.append((x, y))

pri_list = []
# 첫 번째부터 모든 경우의 수를 탐색하기
for i in range(N):
    # x는 x끼리, y는 y끼리 비교
    # 우선 자기보다 큰 덩치가 안나오면 등수는 1로 시작
    priority = 1
    for j in range(N):
        # 자기 자신과의 비교는 제외
        if i == j:
            continue
        else:
            # 비교 대상이 자신보다 큰 덩치인경우 등수+1
            if my_list[j][0] > my_list[i][0] and my_list[j][1] > my_list[i][1]:
                priority += 1
    pri_list.append(priority)

print(' '.join(map(str, pri_list)))
            
    
    