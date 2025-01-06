N = int(input())
road_list = list(map(int,input().split()))
pay_list = list(map(int,input().split()))

i=0
total_pay = 0
while i < N-1:
    if pay_list[i] > pay_list[i+1]:
        total_pay += pay_list[i]*road_list[i]
        i +=1
    else:
        pay_list[i+1] = pay_list[i]
        i +=1

total_pay = sum([i*j for i,j in zip(road_list,pay_list)])

        
print(total_pay)