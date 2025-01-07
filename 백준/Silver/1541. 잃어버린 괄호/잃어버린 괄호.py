# 문자열 입력받기 ex, 55-35+30-50+50+50-50
N=input()


##### 풀이 아이디어 #####
# 괄호를 사용하여 최소값 만들기
# 1. -부호 뒤에 있는 +로 묶인 숫자들을 괄호로 묶는다. (모아서 뺀다는 개념)
# 2. 즉, 첫 숫자 + (-로 묶을 수 있는 모든 수들) 이면 끝
num = list(N.split('-'))


value = 0

# 첫 문자열이 -로 시작하는 경우, 처음엔 '' 빈 문자열이 들어옴
if num[0] == '':
    
    for i in range(1,len(num)):
        value -= sum(map(int,num[i].split('+')))

else:
    value += sum(map(int,num[0].split('+')))

    for i in range(1,len(num)):
        value -= sum(map(int,num[i].split('+')))


print(value)