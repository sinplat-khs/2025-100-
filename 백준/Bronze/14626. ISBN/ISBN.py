# 입력받기
input_str = input()

# 규칙에 맞게 일단 더하기
check_num = 0

# check_num은 나머지 수의 합을 10-(10으로 나눈 나머지)임, 
# 근데 10이면 0으로 출력해야함

my_num = 0
index = 0
for i, ele in enumerate(input_str):
    try:
        if (i)%2 == 0:
            my_num += int(ele)
            
        else:
            my_num += int(ele)*3
    except:
        index = i
        check_num = ele
        continue
        
# my_num은 수의 합, 나머지 하나로 10으로 나누어떨어지는 수 찾기
for num in range(10):
    temp_sum = my_num
    if index % 2 == 0:
        temp_sum += num
    else:
        temp_sum += num*3
        
    m = (10 - (temp_sum%10)) %10
    if m == 0:
        print(num)
        break


