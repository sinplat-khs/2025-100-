# 동전 종류의 수, 만들어야하는 가격 입력받기
N,K = map(int, input().split(' '))

# 동전의 가치 입력받기
value_list = []
while len(value_list) < N:
    value_list.append(int(input()))

# 오름차순으로 전환, 비싼 동전부터 사용해야하기 때문
value_list = value_list[::-1]
value_list

count = 0
# 비싼 동전부터 사용하면서 K에서 빼는 알고리즘 사용
for i in range(N):
    # K 값 충족 완료
    if K == 0:
        break
    # 가장 비싼 동전으로 최대한 빼기
    elif K>=value_list[i]:
        count += K // value_list[i]
        K = K%value_list[i]
    
    # 동전 가치가 더 비싼 경우 사용 못하므로 넘어가기
    else:
        continue
        
print(count)
    