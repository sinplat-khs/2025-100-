# 문제 갯수 입력받기

N = int(input())

##### 풀이 아이디어 #####
# 1. 가장 왼쪽에서부터 ( 한 개를 서치하기
# 2. 그럼 가장 우측에서부터 ( 를 발견한 시점까지 서치하며 )를 찾기
# 3. 둘이 매칭이 된다면 찾은 (와 )를 문자열에서 지우기
# 위 내용 반복
# 2번에서 못찾으면 그대로 break

# def search_couple(input_str):
#    while True:
#        found = False # 매칭이 됐는지 체크
#        for i in range(len(input_str)):
#            if input_str[i] == '(':            
#                for j in range(i+1,len(input_str)):
#                    if input_str[j] == ')':
#                        input_str = input_str[:i] + input_str[i+1:j] + input_str[j+1:]
#                        found = True # 매칭이 된 상황
#                        break
#                if found: # 매칭을 했으면 처음부터 다시 탐색해야됨
#                    break
#        if not found: # 매칭이 되는 게 없으면 종료
#            break
#    return 'YES' if found else 'NO'
                

# for i in range(N):
#    input_str = str(input())
#    print(search_couple(input_str))



# 방식을 다르게, 모든 괄호가 서로 매칭이 돼야하는 문제임
# 왼쪽부터 훑으면서 ( 가 나오는 경우 list에 추가
# ) 가 나오는 경우에 만약 list에 (가 있으면 없애기
# 만약 없으면 return 'NO' 맨 왼쪽에 )만 있으면 매칭이 불가하기 때문

def search_couple(input_str):
    my_list = []
    
    for ele in input_str:
        if ele == '(':
            my_list.append(ele)
        elif ele == ')':
            if my_list:
                my_list.pop()
            else:
                return 'NO'
     
    return 'YES' if not my_list else 'NO'


for _ in range(N):
    input_str = str(input().strip())
    print(search_couple(input_str))
            
                    
                    
                    
                
                