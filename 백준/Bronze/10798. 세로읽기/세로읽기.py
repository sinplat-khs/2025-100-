# 입력받은 문자들을 배열로 만들어서 저장해두기
# 저장된 배열을 인덱스를 늘려가며 출력하기
# 없는 인덱스는 pass
# 빈 배열 생성

my_tensor = []

# 입력받기
for i in range(5):
    my_str = input()
    my_list = list(my_str)
    
    my_tensor.append(my_list)

    
# 가장 긴 배열 길이 찾기
max_len = max(len(row) for row in my_tensor)

# 세로로 읽기
for i in range(max_len):
    for j in range(5):
        # 현재 열 번호가 my_tensor에 존재하는 경우에만
        if i < len(my_tensor[j]):
            print(my_tensor[j][i], end = '') # 공백없이
        
    
    