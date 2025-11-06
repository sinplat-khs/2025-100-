# 입력받기

T = int(input())

# 거스름돈 리스트 저장
C_list = []
for _ in range(T):
    C_list.append(input())
    
# 쿼터 0.25, 다임 0.1, 니켈 0.05, 페니 0.01
# 달러는 쿼터 25 다임 10 니켈 5 페니 1
# 입력받은 걸 25 로 나눈 나머지 를 10으로 나눈 나머지를 ...

answer_list = []
for case in C_list:
    # 쿼터 추가
    my_num = int(case)
    answer_list.append(my_num//25)
    my_num = my_num%25
    
    # 다임 추가
    answer_list.append(my_num//10)
    my_num = my_num%10
    
    # 니켈 추가
    answer_list.append(my_num//5)
    my_num = my_num%5
    
    # 페니 추가
    answer_list.append(my_num)
    
    for num in answer_list:
        print(num, end = ' ')
        
    answer_list = []
    
    