from collections import deque
import sys

test_num = int(sys.stdin.readline().strip())


# test_num 갯수만큼 테스트 실행
for _ in range(test_num):
    # 1,0
    # 5
    # 위와같이 입력받는 경우
    # 1개의 문서, 타겟문서는 0번째 index
    # 5는 문서의 중요도
    # 0번째 index부터 체크하면서 나머지 문서들 중 중요도가 높은게 있으면 뒤로 이동
    # 없으면 바로 인쇄
    
    N, M = map(int, sys.stdin.readline().strip().split())
    
    importances = deque(map(int, sys.stdin.readline().strip().split()))
    
    # 기존 요소들의 index 기억을 위한 deque 생성
    ori_deque = deque(enumerate(importances))
    
    # 중요도 내림차순
    sorted_importances = sorted(importances, reverse = True)
    
    # print 순서
    print_ord = 0
    
    
    while len(ori_deque) != 0:
        ori_idx, ele = ori_deque.popleft() # 원래 순서, 중요도문서
        
        # 현재 요소가 중요도가 높은지 체크후 끝으로 이동
        if ele < sorted_importances[0]:
            ori_deque.append((ori_idx,ele))
            
        else:
            print_ord += 1
            sorted_importances.pop(0) # 사용된 문서
            
            # 찾고 있던 문서가 맞을 때만 출력
            if ori_idx == M:
                print(print_ord)
                break
    