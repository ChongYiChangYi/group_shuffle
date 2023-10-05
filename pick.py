import numpy as np
import time

n = int(input('반 숫자를 입력해주세요 : '))
team1 = [[],[],[],[]]
team2 = [[],[],[],[]]
dict_student1 = {'김수현':0, '이시현':0, '김영준':0, '최연우':0,'김희윤':0,'남현호':0,'이시훈':0,'방준서':0,'선재민':0,'이준휘':0,'전민제':0,'김서연':0,'정서윤':0,'조세환':0,'최준우':0}
dict_student2 = {'문도현':0, '이재홍':0, '정우진':0, '유승민':0,'손동욱':0,'이유정':0,'김지환':0,'남도현':0,'목진우':0,'박준현':0,'김정래':0,'이상학':0,'배요한':0,'이동령':0,'이우진':0}
list_student1 = list(dict_student1)
list_student2 = list(dict_student2)
if n ==1:
  np.random.seed(seed=int(time.time()))
  np.random.shuffle(list_student1)
  dict_student1 = {student: dict_student1[student] for student in list_student1}
  dict_student1 = dict(sorted(dict_student1.items(), key= lambda x:x[1]))
  list_student1 = list(dict_student1)
  for i in range(15):
    if i <= 2:
        team1[0].append(list_student1[i])
        dict_student1[list_student1[i]] += 1
    elif i<= 6:
        team1[1].append(list_student1[i])
    elif i<=10:
        team1[2].append(list_student1[i])
    else:
        team1[3].append(list_student1[i])
  for num, item in enumerate(team1, start=1):
    print(f'{num}조 : ', end='')
    print(*item, sep = ', ')
  print(dict_student1)
if n ==2:
  np.random.seed(seed=int(time.time()))
  np.random.shuffle(list_student2)
  dict_student2 = {student: dict_student2[student] for student in list_student2}
  dict_student2 = dict(sorted(dict_student2.items(), key= lambda x:x[1]))
  list_student2 = list(dict_student2)
  for i in range(15):
    if i <= 2:
        team2[0].append(list_student2[i])
        dict_student2[list_student2[i]] += 1
    elif i<= 6:
        team2[1].append(list_student2[i])
    elif i<=10:
        team2[2].append(list_student2[i])
    else:
        team2[3].append(list_student2[i])
  for num, item in enumerate(team2, start=1):
    print(f'{num}조 : ', end='')
    print(*item, sep = ', ')
  print(dict_student2)
