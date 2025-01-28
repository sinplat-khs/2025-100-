#  0 0 0을 입력받기 전까지는 계속 입력받기

while True:
    a, b, c = map(int,input().split())
    
    # 0 0 0 입력받을 시 loop 탈출
    if a==0 and b==0 and c==0:
        break
    
    # 가장 긴 변과 나머지 두 변을 정렬하기 위해 list 사용하기
    my_list = [a,b,c]
    
    my_list = sorted(my_list)
    
    max_num = my_list[-1]
    num1,num2 = my_list[:2]
    
    
    # 피타고라스 정리 사용
    
    if (max_num**2) == (num1**2) + (num2**2):
        print('right')
    else:
        print('wrong')
