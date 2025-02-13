# 문제 입력받기
# => input 관련 valueError 예상됨
# sys.stdin.read() 로 개선하기
import sys
input_value = sys.stdin.read().split()

N = int(input_value[0])
my_list1 = list(map(int,input_value[1:N+1]))

M = int(input_value[N+1])
my_list2 = list(map(int,input_value[N+2:]))

    
# 풀이 아이디어
# M 개의 입력값에 대해 my_list1에 존재하는 갯수만큼 return 필요

# for ele in my_list2:
#    stack = 0
#    while True:
#        if ele in my_list1:
#            stack += 1 
#            my_list1.remove(ele)
#        else:
#            print(stack)
#            break
        
        
# => ValueError 발생
# => Collections Counter 사용하는 방법으로 수정
# => 시간복잡도 O(N*M) 에서 O(N+M) 으로 축소 가능

from collections import Counter

counter = Counter(my_list1) # 각 요소의 갯수를 딕셔너리 형태로 반환함

for ele in my_list2:
    print(counter.get(ele, 0)) # 존재하면 값 출력, 없으면 0출력
