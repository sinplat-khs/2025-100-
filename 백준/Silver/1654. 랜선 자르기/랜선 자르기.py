# 가지고 있는 랜선 수 K, 필요한 랜선 수 N 입력받기
K, N = map(int, input().split())

# 가지고 있는 랜선 길이 입력받기
length_list = []
for i in range(K):
    length_list.append(int(input()))

# 이진 탐색을 위한 범위 초기화
start = 1
end = max(length_list)

def binary_search(array, start, end, N):
    result = 0  # 최대 랜선 길이를 저장할 변수
    while start <= end:
        mid = (start + end) // 2
        count = sum(length // mid for length in array)  # mid 길이로 자른 랜선 개수의 합

        if count >= N:  # 필요한 랜선 수보다 많거나 같으면
            result = mid  # 현재 길이를 저장하고 더 긴 길이를 탐색
            start = mid + 1
        else:  # 부족하면 더 짧게 자름
            end = mid - 1
    return result

# 최대 랜선 길이 출력
print(binary_search(length_list, start, end, N))