# 입력받기

a,b,c = map(int,input().split())

my_list = [a,b,c]


# 최대값 기준으로 생각하기
max_value = max(my_list)
my_list.remove(max_value)

# 남은 두 변의 합이 max_value보다 크면 그대로 더하기
if sum(my_list) > max_value:
    print(sum(my_list) + max_value)
    
# 두 변의 합이 더 작으면 두변의 합*2 - 1
else:
    print(sum(my_list)*2 - 1)
    
