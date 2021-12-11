# 수리가 가능한 제품->6개, 에어컨 실외기 냉장고 보일러 샷시 조명
# 수리 업체->6개, 업체A, 업체B, 업체C, 업체D, 업체E, 업체F

# Input
# 사용자가 Q를 입력할때까지 수리할 제품명을 입력받습니다.
# 제품명은 여섯개까지만 입력받을 수 있고, 똑같은 제품을 두번 입력했다면 이미 입력한 제품이라는 메세지를 출력해야 합니다.
# 수리받고 싶은 제품의 개수만큼 수리받고 싶은 업체를 물어봅니다.

print("\t\t<가격표> (단위: 만원)")
print(" \t에어컨\t실외기\t냉장고\t보일러\t샷시\t조명")
print("A\t20\t12\t18\t12\t230\t37")
print("B\t23\t14\t29\t14\t150\t43")
print("C\t17\t16\t15\t12\t300\t40")
print("D\t19\t13\t23\t11\t220\t35")
print("E\t21\t15\t15\t14\t190\t30")
print("F\t25\t14\t16\t13\t280\t31\n")

product = ["에어컨", "실외기", "냉장고", "보일러", "샷시", "조명"]
company = {"A":[20, 12, 18, 12, 230, 37], "B":[23, 14, 29, 14, 150, 43], "C":[17, 16, 15, 12, 300, 40], "D":[19, 13, 23, 11, 220, 35], "E":[21, 15, 15, 14, 190, 30], "F":[25, 14, 16, 13, 280, 31]}

num = 0
repairProduct = []
while True:
    temp = input("수리할 제품 명을 입력하세요 (종료를 원하면 Q입력) >> ")
    if temp == 'Q':
        break
    elif temp not in product:
        print("에어컨, 실외기, 냉장고, 보일러, 샷시, 조명만 가능합니다.")
        continue
    elif product.index(temp) in repairProduct:
        print("해당 제품은 이미 입력하셨습니다.")
        continue
    else:
        repairProduct.append(product.index(temp))
        num += 1

repairCompany = []
repairCompanyName = []
i1 = 1
while (i1 <= num):
    temp = input("원하는 업체 후보%d는? "%i1)
    if temp not in company.keys():
        print("A, B, C, D, E, F 업체만 가능합니다.")
        continue
    elif company[temp] in repairCompany:
        print("해당 업체는 이미 입력하셨습니다.")
        continue
    else:
        repairCompany.append(company[temp])
        repairCompanyName.append(temp)
        i1 += 1


# Processing
for i in range(num):
    for j in range(6):
        if j not in repairProduct:
            repairCompany[i][j] = 0
for i in range(num):
    while (0 in repairCompany[i]):
        repairCompany[i].remove(0)

selected = []

def promising(selected, arr, n): # 선택된 열들을 제외하고 가장 유망한 열을 제시해주는 함수
    candidate = {}
    for s in range(num):
        temp = 0
        if s in selected:
            continue
        else:
            selected.append(s)
            temp += arr[n][s]
            for i in range(n+1, num):
                min = 1000
                for j in range(num):
                    if j in selected:
                        continue
                    else:
                        if arr[i][j] < min:
                            min = arr[i][j]
                temp += min
            candidate[s] = temp
            selected.remove(s)
    
    final = list(candidate.keys())[0]
    for index in candidate:
        if candidate[index] < candidate[final]:
            final = index

    return final

for i in range(num-1):
    selected.append(promising(selected, repairCompany, i))

for i in range(num):
    if i not in selected:
        selected.append(i)


# Output
# 제품 하나당 업체를 하나씩 추천해주는 조합을 출력합니다.

print("\n<업체 추천 조합>")

selected.reverse()
for i in range(num):
    print("업체%s : %s"%(repairCompanyName[i], product[repairProduct[selected.pop()]]))