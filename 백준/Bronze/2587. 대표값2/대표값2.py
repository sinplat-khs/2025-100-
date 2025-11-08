# 다섯 줄 입력받기

my_list = []
for _ in range(5):
    my_list.append(int(input()))


# 크기순 정렬
len_list = len(my_list)

my_list.sort()

print(int(sum(my_list) / len_list))
print(int(my_list[2]))