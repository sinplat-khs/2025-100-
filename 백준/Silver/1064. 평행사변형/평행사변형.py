Xa, Ya, Xb, Yb, Xc,Yc = map(int,input().split())



A = [Xa,Ya]
B = [Xb,Yb]
C = [Xc,Yc]

# (가장 긴 변 - 가장 짧은변) * 2
AB = sum([(x-y)**2 for x ,y in zip(A,B)])**(1/2)
BC = sum([(x-y)**2 for x ,y in zip(B,C)])**(1/2)
CA = sum([(x-y)**2 for x ,y in zip(C,A)])**(1/2)

if (Xa==Xb) or (Xa==Xc):
    if Xb == Xc:
        print(-1)
    else:
        my_list = [AB,BC,CA]
        print(2*(max(my_list) - min(my_list)))   

elif (Ya-Yb)/(Xa-Xb) == (Ya-Yc)/(Xa-Xc):
        print(-1)



else:
    my_list = [AB,BC,CA]
    print(2*(max(my_list) - min(my_list)))