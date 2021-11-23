# Input
# 최소주문금액
# 장바구니 리스트 [ [상품명, 가격], ..., [상품명, 가격] ]
# 한 개의 상품을 여러개 사고 싶다면 상품가격×상품개수로 입력해주셔야합니다.

from typing import final


minimumOrderAmount = int(input("최소 주문 금액 >> "))

print("상품 리스트 입력(Q 종료)(수량이 2개 이상일 경우 수량도 입력) >> ")
shoppingCart = {}
costList = []
index = 1
while True:
    goods = input("%d. "%index).split()

    if goods[0] == 'Q':
        break
    elif len(goods) == 3:
        goods[1] = int(goods[1]) * int(goods[2])
        goods.pop()
    
    if int(goods[1]) not in shoppingCart:
        shoppingCart[int(goods[1])] = []
    shoppingCart[int(goods[1])].append(goods[0])

    if int(goods[1]) not in costList:
        costList.append(int(goods[1]))
    index += 1


# Processing
# 높은 가격순대로, 가격으로만 처리합니다.
# 만약 양념감자와 치즈스틱 모두 2000원이라면 양념감자 따로 치즈스틱 따로 처리하는 것이 아니라 2000원으로 processing을 한뒤 최종 출력에서
#     a버거, 양념감자, 콜라(L) -> 15000원 만족
#     a버거, 치즈스틱, 콜라(L) -> 15000원 만족
# 이런식으로 처리해주시면 될 것 같습니다.
# 입력한 최소주문금액을 만족하는 상품 조합이 없다면, 100원 올려서 다시 조합을 찾습니다.
# 만약 15000원을 만족하는 상품조합이 없다면 15100을 만족하는 조합을 찾고, 15100원을 만족하는 조합이 없으면 15200원 ... 이런식으로 처리해주시면 될 것 같습니다.

costList.sort()

def subset():
    list = []
    for i in range(len(costList)):
        if (include[i]=='y'):
            list.append(costList[i])
    list.reverse()
    MOAList.append(list)

def promising(i, weight, total):
    return (weight+total >= minimumOrderAmount) and ((weight == minimumOrderAmount) or (weight+costList[i+1] <= minimumOrderAmount))

def sum_of_subsets(i, weight, total):
    if promising(i, weight, total):
        if (weight == minimumOrderAmount):
            subset()
        else:
            include[i+1] = 'y'
            sum_of_subsets(i+1, weight+costList[i+1], total-costList[i+1])
            include[i+1] = 'n'
            sum_of_subsets(i+1, weight, total-costList[i+1])

while True:
    MOAList = []
    include = []

    for i in range(len(costList)):
        include.append('n')

    sum_of_subsets(-1, 0, sum(costList))

    if len(MOAList) == 0:
        print("최소주문금액(%d원)을 만족하는 조합이 없습니다. 100원 올려서 다시 진행합니다."%minimumOrderAmount)
        minimumOrderAmount += 100
    else:
        break


# Output
# 상품1, 상품2, ..., 상품n -> (맞추고자하는 금액) 만족

finalList = []
for list in MOAList:
    nameList = []
    for cost1 in list:
        for cost2 in shoppingCart:
            if cost1 == cost2:
                nameList.append(shoppingCart[cost2])
    
    finalList.append(nameList)

for i in range(len(finalList)):
    for j in range(len(finalList[i])):
        if (len(finalList[i][j]) == 1):
            finalList[i][j] = ''.join(finalList[i][j])
        else:
            finalList[i][j] = ' or '.join(finalList[i][j])

for list in finalList:
    print(', '.join(list), "-> %d원 만족"%minimumOrderAmount)