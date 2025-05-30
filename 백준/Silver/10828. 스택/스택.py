# 줄 수 입력받기
import sys

N = int(sys.stdin.readline().strip())

stack = []

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push':
        stack.append(command[1])
        
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
     
    elif command[0] == 'size':
        print(len(stack))
    
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])