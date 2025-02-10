# 입력받는 갯수 input

N = int(input())

# 나이 / 이름 입력받기
# my_list = []
# for _ in range(N):
#    age, name = input().split()
#    my_list.append([age,name])
    
# my_list의 형태는
# [[age1, naem1], [age2, name2], [age3, name3]  .... ]

# => 들어온 순서 파악을 위해 dict로 하기
# my_dict = {}
# for i, _ in enumerate(range(N)):
#    age, name = input().split()
#    my_dict[i] = [age,name]
    
# my_dict 형태는
# my_dict = {0:[age1,name1], 1:[age2,name2], .... }
# age로 정렬 후 dict의 key로 다음 정렬하기


# ==> dict도 필요없음, 리스트로 순서, 나이, 이름 다저장하기
my_list = []
for i in range(N):
    age, name = input().split()
    my_list.append((int(age), i, name))
    
# my_list 형태 = [[순서, 나이, 이름], [순서,나이,이름], ... ]

# 나이가 같으면 입력 순서 유지하도록
my_list.sort(key = lambda x: (x[0],x[1]))

for age, _, name in my_list:
    print(age, name)
    