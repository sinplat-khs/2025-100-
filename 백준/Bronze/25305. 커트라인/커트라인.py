# 입력받기
N, K = map(int, input().split())


# list로 저장하기
my_list = list(map(int, input().split()))


# 내림차순 정렬
my_list.sort(reverse=True)

# k등의 점수 출력

print(my_list[K-1])