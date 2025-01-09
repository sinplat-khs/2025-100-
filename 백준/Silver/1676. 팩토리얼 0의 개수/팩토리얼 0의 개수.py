# N 입력받기
N = int(input())

# 팩토리얼 구현하기
# 팩토리얼 = Nx(N-1)x(N-2) ... x1
def factorial(num):
    output = 1
    while num > 0:
        output = output*num
        num -= 1
       
    return output
        
##### 풀이 아이디어 #####
# 숫자를 문자열로 변환, 변환 후 뒤에서부터 인덱싱하며 0인지 체크, 0이 아닌 수가 종료

check_value = factorial(N)
check_str = str(check_value)

answer = 0
for i in range(len(check_str)):
    if check_str[::-1][i] == '0':
        answer += 1
    else:
        break
        
print(answer)