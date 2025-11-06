# 입력을 계속 받기 0 0 들어오기 전까지

while True:
    A, B = map(int, input().split())
    
    if A == 0 and B == 0 :
        break
        
        
    # 약배수 여부 확인
    
    # A가 B의 약수인 경우
    if A > B: # A가 큰 경우, A가 B의 배수인지 확인
        if A%B == 0:
            print('multiple')
            
        else:
            print('neither')
    elif A < B: # B가큰 경우, 약수인지 확인
        if B%A == 0:
            print('factor')
        else:
            print('neither')
    