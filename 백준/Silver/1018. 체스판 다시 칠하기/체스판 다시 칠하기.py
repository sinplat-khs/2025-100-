M,N = map(int,input().split())

WB = 'WBWBWBWB'
BW = 'BWBWBWBW'
wb_array = [WB,BW,WB,BW,WB,BW,WB,BW]


my_list =[]
for m in range(M):
    my_list.append(input())
    
my_array1 = []
for m in range(M-7):
    for n in range(N-7):
        my_array1.append(sum([1 for i in range(8) for j in range(8) if (my_list[m+i][n+j]) != (wb_array[i][j])]))
        
my_array2 =[]
for m in range(M-7):
    for n in range(N-7):
        my_array2.append(sum([1 for i in range(8) for j in range(8) if (my_list[m+i][n+j]) != (wb_array[::-1][i][j])]))
        
        
print(min(min(my_array1),min(my_array2)))