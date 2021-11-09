# (조건)
# - 환기를 위해 n시간 비워두기
# - 수용 인원 별로 강의실은 세 가지 종류가 있다
#     - Class 1~10: 40명 강의실 -> (50%인 20명만 실제 수용 가능)
#     - Class 11~20: 60명 강의실 -> (30명만 실제 수용 가능)
#     - Class 21~30: 120명 강의실 -> (60명만 실제 수용 가능)
# - 60명을 초과하는 대형 강의는 온라인 시험을 원칙으로 한다. (60명이 넘는 오프라인 시험은 없다.)

groupA = {}     # class 1~10
for i in range(10):
    groupA[i+1] = []
    for j in range(24):
        groupA[i+1].append(0)

groupB = {}     # class 11~20
for i in range(10):
    groupB[i+11] = []
    for j in range(24):
        groupB[i+11].append(0)

groupC = {}     # class 21~30
for i in range(10):
    groupC[i+21] = []
    for j in range(24):
        groupC[i+21].append(0)

# input
# - 배정할 시험의 개수
# - 강의명, 시험 시작, 종료 시간, 인원
# - 환기 시간

examN = int(input("시험 개수 >> "))
ventilation = int(input("환기 시간 >> "))
print("시험 정보 입력 >> ")
examInfo = {}
for i in range(examN):
    temp = input().split()
    examInfo[temp[0]] = {'시작시간':int(temp[1]), '종료시간':int(temp[2]), '인원':int(temp[3])}


# processing
# task scheduling (최소 cpu 배정 문제)

scheduler = {}
for exam in examInfo:
    if examInfo[exam]['인원'] < 21:
        for room in groupA:
            if sum(groupA[room][examInfo[exam]['시작시간'] : examInfo[exam]['종료시간']+ventilation]) != 0:
                continue
            for i in range(examInfo[exam]['시작시간'], examInfo[exam]['종료시간']+ventilation):
                groupA[room][i] = 1
            if room not in scheduler:
                scheduler[room] = []
            scheduler[room].append(exam + '(' + str(examInfo[exam]['시작시간']) + ',' + str(examInfo[exam]['종료시간']) + ')')            
            break
    elif examInfo[exam]['인원'] < 31:
        for room in groupB:
            if sum(groupB[room][examInfo[exam]['시작시간'] : examInfo[exam]['종료시간']+ventilation]) != 0:
                continue
            for i in range(examInfo[exam]['시작시간'], examInfo[exam]['종료시간']+ventilation):
                groupB[room][i] = 1
            if room not in scheduler:
                scheduler[room] = []
            scheduler[room].append(exam + '(' + str(examInfo[exam]['시작시간']) + ',' + str(examInfo[exam]['종료시간']) + ')')  
            break
    elif examInfo[exam]['인원'] < 61:
        for room in groupC:
            if sum(groupC[room][examInfo[exam]['시작시간'] : examInfo[exam]['종료시간']+ventilation]) != 0:
                continue
            for i in range(examInfo[exam]['시작시간'], examInfo[exam]['종료시간']+ventilation):
                groupC[room][i] = 1
            if room not in scheduler:
                scheduler[room] = []
            scheduler[room].append(exam + '(' + str(examInfo[exam]['시작시간']) + ',' + str(examInfo[exam]['종료시간']) + ')')  
            break
    else:
        if '온라인' not in scheduler:
            scheduler['온라인'] = []
        scheduler['온라인'].append(exam + '(' + str(examInfo[exam]['시작시간']) + ',' + str(examInfo[exam]['종료시간']) + ')')


# output
# - 최소 배정 강의실 수
# - 강의실별 시험 스케줄 출력

if '온라인' in scheduler:
    print("\n총 %d개 강의실이 필요합니다.\n"%(len(scheduler) - 1))
    print("온라인: ", " ".join(scheduler['온라인']))
else:
    print("\n총 %d개 강의실이 필요합니다.\n"%len(scheduler))
for room in scheduler:
    if room != '온라인':
        print("Class %d: "%room, " ".join(scheduler[room]))