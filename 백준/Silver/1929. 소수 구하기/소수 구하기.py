M,N = map(int,input().split())

my_list = [True]*(N+1)

for i in range(2,int(N/2) +1):
    if my_list[i] ==True:
        for j in range(i+i,N+1,i):
            my_list[j]=False

for num in [i for i in range(2,N+1) if (my_list[i]==True) and (i>=M)]:
    print(num)

