# 문제 설명이 모호하여 재해석
# 1부터 N까지 숫자를 input받음
# 그걸 스택에 쌓는 걸 push(+) 라고 함
# 후입선출 기준으로 pop(-)을 할 수 있음
# N개의 입력이 있을텐데, 이 입력 순서를 찾기위해 push(+), pop(-) 해야되는 순서대로 출력한다.

N = int(input())

stack_list = []
max_stack = 0
possible = True
push_pop_list = []

for _ in range(N):
    k = int(input())
    
    
    # 입력받은 k가 지금까지 확인한 숫자보다 크면 쌓기, 작으면 확인으로 넘어감
    while max_stack < k:
        max_stack += 1
        stack_list.append(max_stack)
        push_pop_list.append('+')
    
    # 비어있는지 확인 + 마지막 요소가 k와 같으면
    if stack_list and stack_list[-1] == k:
        stack_list.pop()
        push_pop_list.append('-')
    else:
        possible = False
        break
        
    
if possible:
    for ele in push_pop_list:
        print(ele)
else:
    print('NO')
    
        
        
            
    
    