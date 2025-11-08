# 입력받기

N = int(input())

# 리스트 저장

my_list = list(map(int,(input().split())))

# 리스트 값의 종류를 세기
my_set = set(my_list)

unique_list = list(my_set)
unique_list.sort()

my_dict = {value:idx for idx, value in enumerate(unique_list)}


# 밸류 : 순위로 저장돼있음

for ele in my_list:
    print(my_dict[ele], end = ' ')

"""
unique_len = len(list(my_set))

# 내림차순
unique_list.sort(reverse=True)

my_list2 = []
# unique_len-1 값부터 최대값에 할당하기
for ele in my_list:
    # unique_list의 값과 비교해서 매칭되는 index 값으로 부여하기
    for i, unique_value in enumerate(unique_list):
        if unique_value == ele:
            my_list2.append(i)
            
for ele in my_list2:
    print(ele, end= ' ')

"""