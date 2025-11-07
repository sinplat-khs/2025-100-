N = int(input())
end_time = 0
time_list= []
count=0
for i in range(N):
    start,end = map(int,input().split(' '))
    time_list.append([start,end])
    
time_list = sorted(time_list, key = lambda time:(time[1],time[0]))

for i in range(N):
    if end_time <= time_list[i][0]:
        count+=1
        end_time = time_list[i][1]
    else:
        continue
        
print(count)