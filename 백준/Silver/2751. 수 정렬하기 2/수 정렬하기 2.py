# 수의 갯수 input
import sys

# input 속도 개선을 위한 재선언
input = sys.stdin.read

# 데이터 list화
data = input().split() 

N = int(data[0])

# 나머지를 정수로 변환 후 정렬

my_list = sorted(map(int,data[1:]))

# 수 list 받기
# my_list = []
# for i in range(N):
#     my_list.append(input())

# 결과 출력
sys.stdout.write('\n'.join(map(str,my_list)) + '\n')