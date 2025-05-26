import sys
from collections import deque, Counter
from statistics import mean, median

N = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
num_list = deque(num_list)

# 산술평균 출력
print(round(mean(num_list)))

# 중앙값 출력
num_list = sorted(num_list)
print(median(num_list))

# 최빈값 출력
counts = Counter(num_list)
common_nums = counts.most_common()
highest_freq = common_nums[0][1]
modes = [x for x, y in common_nums if y == highest_freq]
modes = sorted(modes)
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# 범위 출력 (최대값 - 최소값)
print(max(num_list) - min(num_list))