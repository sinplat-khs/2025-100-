# 입력받기
N = int(input())

my_list = []

for _ in range(N):
    my_list.append(int(input()))
    
    
my_list.sort(reverse = False)


for ele in my_list:
    print(ele)