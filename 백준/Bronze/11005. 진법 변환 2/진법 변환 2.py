# N, B 입력받기

N, B = map(int,input().split())

# 변환할 문자 미리 생성
my_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 빈 문자열 만들어두기
answer = ""

# 입력받은 N을 모두 소모해서 answer 만들기

while N > 0:
    # N을 B진법으로 나눈 나머지, 예 34면 my_str의 34번재 [인덱스 33] 더하기
    answer = my_str[N % B] + answer
    # 몫만 남음
    N = N//B
    
print(answer)