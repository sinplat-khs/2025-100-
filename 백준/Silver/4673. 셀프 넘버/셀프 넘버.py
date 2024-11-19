def d(n):
    return n+sum([int(str(n)[i]) for i in range(len(str(n)))])

my_list = [d(x+1) for x in range(10000)]

for i in range(1,10001):
    if i in my_list:
        pass
    else:
        print(i)