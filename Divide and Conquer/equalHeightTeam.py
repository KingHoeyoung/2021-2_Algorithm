""" 
Input: 학생 수(짝/홀), 이름, 학생별 키

Processing: 
Pivot은 키 평균 내어서 평균 키에 가장 가까운 학생으로 선택.
Pivot 기준으로 왼쪽은 작은 키들의 모임(1모둠) (ex.1,2,3,4) pivot: 5
Pivot 기준으로 오른쪽은 큰 키들의 모임(2모둠) (ex.6,7,8,9)
(1모둠 1명 - 2모둠 1명)씩 뽑아서 A/B팀으로 구성 [학생 수 홀수라면 merge 전 최종 pivot 학생은 심판]
ex) A팀에 첫번째로 1모둠에서 1명, 두번째로 2모둠에서 1명, 세번째로 1모둠에서 1명...
    B팀에 첫번째로 2모둠에서 1명, 두번째로 1모둠에서 1명, 세번째로 2모둠에서 1명... 

Output: 키 순 나열(오름차순)이되 출력은 이름으로
"""
import random

def avr_closest(dic):
    nameL = dic.keys()
    heightL = dic.values()
    avr = sum(heightL)/len(dic)
    closest = avr
    for name in nameL:
        temp = abs(avr-dic[name])
        if temp<=closest:
            closest = temp
            pivot = name
    return pivot

def quick_sort(dic):
    if len(dic) <= 1:
        return dic
    pivot = avr_closest(dic)
    lesser, equal, greater = {}, {}, {}
    for name in dic.keys():
        if dic[name] < dic[pivot]:
            lesser[name] = dic[name]
        elif dic[name] > dic[pivot]:
            greater[name] = dic[name]
        else:
            equal[name] = dic[name]
    return {**quick_sort(lesser), **equal, **quick_sort(greater)}


#input
studentsNum = int(input("학생 수를 입력해주세요 >> "))
students = {}
for i in range(studentsNum):
    studentName = input("%d번째 학생 이름을 입력해주세요 >> "%(i+1))
    studentHeight = int(input("%d번째 학생 키를 입력해주세요 >> "%(i+1)))
    students[studentName] = studentHeight


#processing
pivot = avr_closest(students)
sorted_students = list(quick_sort(students).items())
#print(sorted_students)

for i in range(studentsNum):
    if sorted_students[i][0] == pivot:
        pivot = i
        break
if (studentsNum % 2 == 0):
    team1 = sorted_students[:pivot]
    team2 = sorted_students[pivot:]
    #print(team1, team2)
else:
    judge = sorted_students[pivot] #튜플
    team1 = sorted_students[:pivot]
    team2 = sorted_students[pivot+1:]
    #print(team1, judge, team2)

random.shuffle(team1)
random.shuffle(team2)
teamA_list, teamB_list = [], []
for i in range(len(team1)):
    if i%2==0:
        teamA_list.append(team1.pop())
        teamB_list.append(team2.pop())
    else:
        teamA_list.append(team2.pop())
        teamB_list.append(team1.pop())

teamA, teamB = {}, {}
for i in range(len(teamA_list)):
    teamA[teamA_list[i][0]] = teamA_list[i][1]
    teamB[teamB_list[i][0]] = teamB_list[i][1]

teamA_name = list(quick_sort(teamA).keys())
teamB_name = list(quick_sort(teamB).keys())


#output
if (studentsNum % 2 == 0):
    print("")
    print("최종 팀 A >> ", teamA_name)
    print("최종 팀 B >> ", teamB_name)
else:
    print("")
    print("심판 >> ", judge[0])
    print("최종 팀 A >> ", teamA_name)
    print("최종 팀 B >> ", teamB_name)