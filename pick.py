# 테스트
import numpy as np
import time

dict_student = {'김수현':0, '이시현':0, '김영준':0, '최연우':0,'김희윤':1,'남현호':0,'이시훈':1,'방준서':1,'선재민':0,'이준휘':0,'전민제':0,'김서연':0,'정서윤':0,'조세환':0,'최준우':0}
list_student = list(dict_student)
team_num = [3,4,4,4]
team = [[],[],[],[]]
np.random.seed(seed=int(time.time()))
np.random.shuffle(list_student)
dict_student = {student: dict_student[student] for student in list_student}
dict_student = dict(sorted(dict_student.items(), key= lambda x:x[1]))


for i in range(15):
    if i <= 2:
        team[0].append(list_student[i])
        dict_student[list_student[i]] += 1
    elif i<= 6:
        team[1].append(list_student[i])
    elif i<=10:
        team[2].append(list_student[i])
    else:
        team[3].append(list_student[i])


for num, item in enumerate(team, start=1):
    print(f'{num}조 : ', end='')
    print(*item, sep = ',')
print(dict_student)