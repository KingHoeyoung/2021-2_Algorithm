import heapq

print("********** 재고 관리 **********")

# Input
# 물품의 수 N을 입력받는다
# 상품의 이름과 유통기한을 입력받는다

N = int(input("물품 개수 >> "))
inventory = {}
for i in range(N):
    name = input("%d번째 물품 이름 >> "%(i+1))
    if name not in inventory.keys():
        inventory[name] = []
    date = int(input("%d번째 물품 유통기한 >> "%(i+1)))
    inventory[name].append(date)

# Process
# 최소힙을 이용하여 상품들을 유통기한이 빠른 순으로 트리 구조화하고
# 사용자가 입력하는 값에 따라 최소힙에서 상품들을 출력하고 제거해나간다.
# Output
# G (상품명) : 재고가 여러개면 유통기한이 가장 빠른 상품 출력 & 제거 / 없으면 없다고 출력
# Q : 프로그램 종료

print("\n************ HELP ************")
print("1. 재고 확인 : G (상품명)")
print("2. 프로그램 종료 : Q")
print("******************************")

while True:
    command = input(">> ").split()
    
    if command[0] == 'G':
        # 상품이름을 딕셔너리에서 찾고
        # 그 밸류를 최소힙으로 변환하고
        finding_name = command[1]
        if finding_name not in inventory.keys():
            print("-> 없어요!")
        elif inventory[finding_name] == []:
            print("-> 없어요!")
        else:
            heapq.heapify(inventory[finding_name])
            print("->", finding_name, heapq.heappop(inventory[finding_name]))

    elif command[0] == 'Q':
        break

    else:
        print("-> 명령어를 제대로 입력해주세요!")