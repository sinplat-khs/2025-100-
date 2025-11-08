# 입력받기

N = int(input())

# 입력받은 걸 각 자리수로 분리
my_str = str(N)
my_list = list(my_str)
my_int_list = [int(x) for x in my_list]

my_int_list.sort(reverse = True) # 내림차순으로 정렬된 list

my_int_list_str = [str(x) for x in my_int_list]

answer_str = ''.join(my_int_list_str)

print(int(answer_str))
