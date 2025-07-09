# 입력받기
input_str = str(input())

# 풀이 아이디어
# 0번 인덱스부터 시작해서 -1번 인덱스와 비교하며 n/2 까지 반복해서 걸리면 0으로 바꾸기
# 안 걸리면 그대로 1 출력

repeat_num = len(input_str) // 2

answer = 1
for i in range(repeat_num):
    if input_str[i] == input_str[-1-i]:
        pass
    else:
        answer = 0
print(answer)