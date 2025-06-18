T = int(input())


# 테스트 케이스 수 만큼 list에 추가
# -> 미리 테스트 케이스 수 계산해두기 
my_list = []
for _ in range(T):
    ele = int(input())
    my_list.append(ele)
    
max_value = 40

# 0 ~ 40 까지 숫자 0이 출력되는 횟수를 미리 저장
count_0 = [0] * (max_value + 1)
# 0 ~ 40 까지
count_1 = [0] * (max_value + 1)

# -> 우선 0 수행 시 0은 1회, 1은 0회
count_0[0] = 1
count_1[1] = 0

# -> 1 수행 시에는 0은 0, 1은 1
count_0[1] = 0
count_1[1] = 1

# 2 이상의 수는 쪼개서 미리 저장해둔 케이스를 호출할 수 있도록 구성

for i in range(2, max_value + 1):
    count_0[i] = count_0[i-1] + count_0[i-2]
    count_1[i] = count_1[i-1] + count_1[i-2]

# 각 케이스에 대해 결과 출력
for n in my_list:
    print(count_0[n], count_1[n])