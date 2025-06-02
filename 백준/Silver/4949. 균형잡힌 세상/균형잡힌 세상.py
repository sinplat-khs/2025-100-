import sys

#남은 게 있으면 no, 없으면 yes로

# . 하나 받으면 break되는 while문

while True:
    input_line = input()
    if input_line =='.':
        break
    stack = []
    is_true = True
    for ele in input_line:
        # 왼쪽 닫음
        if ele in '([':
            stack.append(ele)
        # 오른족 닫음이 먼저 들어와버리는 경우
        elif ele == ')':
            if not stack or stack[-1] != '(':
                is_true = False
                break
            stack.pop()
        elif ele == ']':
            if not stack or stack[-1] != '[':
                is_true = False
                break
            stack.pop()
    # stack에 아무것도 안쌓인 경우 = 즉 좌우 균형이 맞음 -> yes 아니면 no
    if is_true and len(stack) == 0:
        print('yes')
    else:
        print('no')