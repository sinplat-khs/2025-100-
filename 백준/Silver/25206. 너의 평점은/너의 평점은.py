# 20과목에 대한 입력받기

# 미리 등급 별 학점 지정해두기
my_score = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0
}

my_list = []
init_point = 0
# 
for _ in range(20):
    subject_name, point, grade = str(input()).split(' ')
    if grade == 'P':
        continue
    
    init_point += float(point)
    
    my_list.append(my_score[grade]*float(point))
    
if init_point == 0:
    print(0.000000)
else:
    print(f'{sum(my_list)/init_point:.6f}')
