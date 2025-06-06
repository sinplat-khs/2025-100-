# 설탕은 3, 5로만 이루어진 봉지
# 배달해야되는 킬로그램 수 N으로 입력받기
N = int(input())

# 봉지의 갯수
count = 0
# 무게
weight = 0

######## 풀이 아이디어 ########
# 최소 봉지 수가 필요하니, 5로 먼저 나눠본다.
# 나머지가 3으로 나눠진다면 그대로 3으로 나눈 뒤 몫을 더해서 출력
# 만약 3으로 안나눠진다면 5로 나눈 봉지 하나를 반환
# 반복 후 3으로 나눠지는 수가 된다면 그대로 3으로 나눈 뒤 몫 더해서 출력


# 5로 먼저 나눠보기
count += int(N//5)

# 현재 무게
weight += count * 5

# 현재 무게가 배달해야되는(N) 무게가 될 떄까지 반복
while (0<= weight <= N):
    # 만약 5로 먼저 나눠본 값이 3으로 나눠지면
    # 그대로 몫 더해서 출력
    if (N-weight)%3 == 0:
        count += int((N-weight)//3)
        weight += count*3
        print(count)
        break
    
    # 3으로 안나눠지는 경우
    # 5를 한 번 빼서 다시 나눠보기
    # 봉지 수는 1 빼야함
    else:
        weight -=5
        count -=1

# 답이 없는 경우 5를 빼다가 음수가 될텐데 이 경우엔 -1 출력하기
else:
    print(-1)

