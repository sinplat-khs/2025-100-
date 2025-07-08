# 입력받기

T = int(input())

# Test 케이스만큼 연속 입력받기
# indexing 활용, 첫 글자 끝 글자 출력
for _ in range(T):
    string = str(input())
    print(f'{string[0]}{string[-1]}')