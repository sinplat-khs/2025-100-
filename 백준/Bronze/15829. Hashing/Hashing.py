R = 31
M = 1234567891

my_num = 0 

# 문자열에 숫자 부여 필요

L = int(input())
s = input()

for i in range(L):
    a_i = ord(s[i])
    # 아스키 코드 반환 => a를 1로 취급해서 시작하기
    a_i = a_i - ord('a') + 1
    
    my_num += a_i * pow(R, i)
    
    my_num %= M
    
print(my_num)
    

    