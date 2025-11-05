# N, B 입력받기

N, B = input().split()

# 문자열인 경우 변환하는 함수
def str_to_num(_input):
    if _input.isdigit():
        return int(_input)
    else:
        return ord(_input.upper()) - ord('A') + 10


# B진법 10진법으로 바꾸기 구현
answer = 0
for ele in N:
    answer = answer*int(B) + str_to_num(ele)

print(answer)