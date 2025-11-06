# 계속 입력받기 -1 받으면 끝

def perfect(n):
    my_list = []
    # 1부터 N까지 나눠지는 수 찾기
    
    d



while True:
    my_list = []
    n = int(input())
    
    if n == -1:
        break
        
        
    else:
        for i in range(1, n):
            if n%i == 0:
                my_list.append(i)
        
        if sum(my_list) == n:
            print(f'{n} = {" + ".join(map(str, my_list))}')
        else:
            print(f'{n} is NOT perfect.')
                
            
        