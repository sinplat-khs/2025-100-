# 반올림 사용을 위한 math, decimal 모듈 사용
import math
import decimal

# 일반적인 반올림의 경우 0.1 ~ 0.4  = 0 , 0.5~ 0.9 = 1
# python의 경우 x.5 에서 가장 가까운 "짝수"로 반올림
# 위와 같은 반올림 방법을 "은행원의 반올림" 이라고 함

# decimal 모듈
# 컴퓨터가 소수 연산 시 발생할 수 있는 연산 오류 보정
# 예) 0.5 -> 컴퓨터가 표현하는 값은 0.500000000000000123

# 시간초과 방지를 위한 sys.stdin.readline() 사용
import sys


n = int(input())
my_list = []
for i in range(n):
    # a = input() input 함수 사용 시 시간초과 발생
    a = sys.stdin.readline()
    my_list.append(int(a))

if n == 0:
    print(0)
else:
    
    # 모든 소수에 decimal.Decimal로 묶어서 인간이 이해하는 소수로 변환
    top = decimal.Decimal(decimal.Decimal(n*15) / decimal.Decimal(100)) + decimal.Decimal(0.5)
    # 반올림
    top = math.floor(float(top))
    
    # 30% 절사된 리스트 반환
    my_list = sorted(my_list)[top:n-top]
    
    # 평균 계산을 위한 합계
    my_sum = sum(my_list)
    
    # 나누기 역시 decimal로 소수변환 필요
    aver = decimal.Decimal(sum(my_list)/len(my_list)) + decimal.Decimal(0.5)
    
    # 반올림 후 마무리
    aver = math.floor(float(aver))
    print(aver)