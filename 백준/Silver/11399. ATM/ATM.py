# N 갯수 input으로 받기
N = int(input())

# N 갯수 만큼 값 받기
my_list = list(map(int, input().split(' ')))

# 최솟값부터 정렬
my_list = sorted(my_list)

# 최솟값(0번째)은 N번 더해질 예정
# 그 다음값(1번째)은 N-1 번 더해질 예정
# 그 다음값(2번째)은 N-2 번 더해질 예정
#  ....
# k번째값은 N-k 번
# N-1번째 값은 1번 더해질 예정
# 즉 my_list[k] * (N-k) for k in range(N) 의 합이 정답

time_list = [(my_list[k])*(N-k) for k in range(N)]

print(sum(time_list))