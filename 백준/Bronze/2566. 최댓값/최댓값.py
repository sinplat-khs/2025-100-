# 배열 생성할 필요 x
# 입력받는 값을 기억해두고, 들어오는 값이 커지면 해당 값의 index와 반복 수 체크 후 출력

my_num = None

answer = [0,0]
# 9줄 입력받기 i+1 = 행
for i in range(9):
    my_list = list(map(int, input().split()))
    # 입력받은 한 줄에서 가장 큰 값 찾기
    # j+1 = 열
    for j, ele in enumerate(my_list):
        if my_num is None:
            my_num = int(ele)
            answer[0] = i+1
            answer[1] = j+1
            
        
        elif int(ele) > my_num:
            my_num = int(ele)
            answer[0] = i+1
            answer[1] = j+1
            
print(my_num)
print(answer[0], answer[1])
            
        