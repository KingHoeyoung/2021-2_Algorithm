# Input
# 첫번째 줄에는 공간의 크기(m*n)을 가로 m과 세로 n으로 입력받습니다.

# 두번째 줄에는 거리두기 단계를 입력받습니다.
# 이 때, 거리두기 단계별로 수행해야 할 기준은 다음과 같습니다.
# 거리두기 1단계: 자리 기준 상하좌우만
# 거리두기 2단계: 자리 기준 상하좌우와 대각선 한칸
# 거리두기 3단계: 상하좌우와 대각선에 있는 모든 칸 비우기

# 세번째 줄에는 고정석 위치의 x좌표와 y좌표를 입력받습다.
# (이때 고정석은 행사의 주최자가 앉을 자리)

size = input("공간 크기 >> ").split()
row = int(size[0])
column = int(size[1])

socialDistance = int(input("거리두기 단계 >> "))

coordinate = input("고정석 좌표 >> ").split()
fixedSeatX = int(coordinate[0])
fixedSeatY = int(coordinate[1])


# Processing
# 거리두기 조건을 만족하면서 공간안에 최대한의 사람을 넣을 수 있는 최적의 해를 Back Tracking Algorithm을 이용해서 구해야 합니다.

seatingGuide = []
for r in range(row+1):
    temp = []
    for c in range(column+1):
        temp.append(0)
    seatingGuide.append(temp)

seatingGuide[fixedSeatX+1][fixedSeatY+1] = 'F'

def socialDistance1(r, c, guide):
    if (guide[r][c+1] == 'F') or (guide[r+1][c] == 'F') or (guide[r][c+1] == 1) or (guide[r+1][c] == 1) or (guide[r+1][c+1] == 'F'):
        if (c != column-1):
            socialDistance1(r, c+1, guide)
        elif (r != row-1):
            socialDistance1(r+1, 0, guide)
    else:
        guide[r+1][c+1] = 1
        if (c != column-1):
            socialDistance1(r, c+1, guide)
        elif (r != row-1):
            socialDistance1(r+1, 0, guide)

def socialDistance2(r, c, guide):
    if (guide[r][c+1] == 'F') or (guide[r+1][c] == 'F') or (guide[r][c] == 'F') or (guide[r][c+1] == 1) or (guide[r+1][c] == 1) or (guide[r][c] == 1) or (guide[r+1][c+1] == 'F'):
        if (c != column-1):
            socialDistance2(r, c+1, guide)
        elif (r != row-1):
            socialDistance2(r+1, 0, guide)
    else:
        guide[r+1][c+1] = 1
        if (c != column-1):
            socialDistance2(r, c+1, guide)
        elif (r != row-1):
            socialDistance2(r+1, 0, guide)

def socialDistance3(r, c, guide):
    if (guide[r+1][c+1] == 'F'):
        if (c != column-1):
            socialDistance3(r, c+1, guide)
        elif (r != row-1):
            socialDistance3(r+1, 0, guide)
    
    flag = 0
    for x in range(column+1):
        if (guide[r+1][x] == 'F') or (guide[r+1][x] == 1):
            flag = 1
    for y in range(row+1):
        if (guide[y][c+1] == 'F') or (guide[y][c+1] == 1):
            flag = 1
    
    # 오른쪽 아래 대각선
    ir = r+2
    ic = c+2
    while (ir <= row) and (ic <= column):
        if (guide[ir][ic] == 'F') or (guide[ir][ic] == 1):
            flag = 1
        ir += 1
        ic += 1
    ir = r
    ic = c
    while (ir >= 0) and (ic >= 0):
        if (guide[ir][ic] == 'F') or (guide[ir][ic] == 1):
            flag = 1
        ir -= 1
        ic -= 1
    
    # 오른쪽 위 대각선
    ir = r+2
    ic = c
    while (ir <= row) and (ic >= 0):
        if (guide[ir][ic] == 'F') or (guide[ir][ic] == 1):
            flag = 1
        ir += 1
        ic -= 1
    ir = r
    ic = c+2
    while (ir >= 0) and (ic <= column):
        if (guide[ir][ic] == 'F') or (guide[ir][ic] == 1):
            flag = 1
        ir -= 1
        ic += 1

    if not flag:
        guide[r+1][c+1] = 1
        if (c != column-1):
            socialDistance3(r, c+1, guide)
        elif (r != row-1):
            socialDistance3(r+1, 0, guide)
    else:
        if (c != column-1):
            socialDistance3(r, c+1, guide)
        elif (r != row-1):
            socialDistance3(r+1, 0, guide)


if socialDistance == 1:     # 1단계
    socialDistance1(0, 0, seatingGuide)
elif socialDistance == 2:   # 2단계
    socialDistance2(0, 0, seatingGuide)
else:                       # 3단계
    socialDistance3(0, 0, seatingGuide)


# Output
# 배치 결과 (사람 있는 곳을 1, 사람 없는 곳을 0)를 행렬의 형식으로 출력
# 인원 수

count = 0
for r in range(row):
    for c in range(column):
        if seatingGuide[r+1][c+1] == 'F' or seatingGuide[r+1][c+1] == 1:
            count += 1

        if c == column-1:
            print(seatingGuide[r+1][c+1])
        else:
            print(seatingGuide[r+1][c+1], end=" ")

print("\n이용할 수 있는 인원은 %d명입니다."%count)