# 입력받기, 0,0,0 이 올 때까지


# 세 변의 상태 체크하기
def check(a,b,c):
    if (a >= b+c) or (b >= a+c) or (c >= a+b):
        return 'Invalid'
    else:
        if (a==b) and (b==c):
            return 'Equilateral'
        else:
            if (a==b) or (b==c) or (c==a):
                return 'Isosceles'
            else:
                return 'Scalene'


while True:
    A, B, C = map(int,input().split())
    
    if (A==0) and (B==0) and (C==0):
        break
        
    else:
        print(check(A,B,C))