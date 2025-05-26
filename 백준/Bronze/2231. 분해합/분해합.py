N = int(input())

# N이 주어진 경우 1부터 N까지 탐색하다가 생성자가 나오면 종료
# 끝까지 생성자가 나오지 않으면 0 출력

answer = 0

for i in range(1, N+1):
    # 문자열로 변환 후, list로 하나하나 요소 생성 후 다시 더하기
    check_num = i
    my_ints = [int(x) for x in str(i)]
    check_num += sum(my_ints)
    
    if check_num == N:
        answer = i
        break
        
print(answer)