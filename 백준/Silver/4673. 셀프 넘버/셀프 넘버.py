# 각 자리 더하는 함수
def d(n):
    # 자기 자신 + 각 자리 str 변환 후 1개씩 int 변환해서 sum 함수로 총합
    return n + sum([int(str(n)[i]) for i in range(len(str(n)))])

# 1부터 9999까지 생성자 만들기, 10000은 무조건 10000보다 큰 숫자이므로 예외
# 여기서 9999보다 더 작은 값이 존재 → 최적화 가능? 9975?
answer_list = [d(x) for x in range(1,10000)]

# 1부터 10000까지, 생성자 있는 건 pass 없는거 print
for i in range(1,10001):
    if i in answer_list:
        pass
    else:
        print(i)