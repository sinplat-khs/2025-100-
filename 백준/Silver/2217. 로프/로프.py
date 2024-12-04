k = int(input())

my_list =[]
for i in range(k):
    b = int(input())
    my_list.append(b)
    
my_list.sort(reverse=True)

value_list =[]
for i in range(k):
    value_list.append(my_list[i]*(i+1))

print(max(value_list))