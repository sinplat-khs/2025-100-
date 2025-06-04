K = int(input())

my_list = []
for _ in range(K):
    input_num = int(input())
    if input_num != 0:
        my_list.append(input_num)
    else:
        if len(my_list) > 0:
            my_list = my_list[:-1]
            
print(sum(my_list))
    
    
    