import sys

# 갯수, 목표수 INPUT
N, max_num = map(int,input().split())

# 입력받아서 list에 저장
my_list = []
my_list = list(map(int, sys.stdin.readline().split()))

# 3개를 택할 수 있는 모든 경우의 수 중 max_num보다 작거나 같으면서 큰 수로 return

# 초기 선언
cur_num = 0

# 첫번째 수 부터 for문
for i in range(len(my_list)):
    # 두번째 수는 첫 번째를 제외 및 첫 번째보다 앞선 수들 제외
    for j in range(i+1, len(my_list)):
        # 세번째도 같은 로직
        for k in range(j+1, len(my_list)):
            total = my_list[i] + my_list[j] + my_list[k]
            
            # 합계가 max_num 보다 작거나 같은 경우 갱신하기 (기존값보다도 작으면 갱신하지 않기)
            if total <= max_num:
                cur_num = max(cur_num,total)
                
                
print(cur_num)

    