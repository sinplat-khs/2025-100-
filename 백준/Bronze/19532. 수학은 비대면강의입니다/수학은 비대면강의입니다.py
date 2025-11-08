# 정수 입력받기
a,b,c,d,e,f = map(int,input().split())

# 연립방정식 풀기

# ax+by = c
# dx+ey = f

# aex + bey = ce
# aex/b + ey = ce/b
# dx + ey = f

# (ae/b - d)x = ce/b - f
# x = (ce/b - f) / (ae/b -d)

# x + (b/a)y = (c/a)
# x + (e/d)y = (f/d)
# (b/a - e/d)y = (c/a - f/d)
# y = (c/a-f/d) / (b/a -e/d)

# 계산하기
if (a*e - b*d) == 0:
    pass
else:
    x = (c*e - b*f) // (a*e - b*d)
    y = (a*f - c*d) // (a*e - b*d)

print(x, y)
