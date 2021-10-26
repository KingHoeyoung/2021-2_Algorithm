"""
Input: 총 인원 수, 사람 명단, constant factor

Processing: 
josephus problem을 이용해 당직표 만들기

Output: 당직 순서 명단
"""
def make_roaster(arr, n, k):
    roaster = []
    index = 0
    for l in range(n):
        index += k - 1
        if index >= len(arr):
            index = index % len(arr)
        roaster.append(arr.pop(index))

    return roaster


for i in range(2):
    if i==0:
        #input
        num = int(input("평일 당직 총 인원 수를 입력해주세요 >> "))
        name_arr = []
        for j in range(num):
            name_arr.append(input("%d번째 사람 이름을 입력해주세요 >> "%(j+1)))
        cf = int(input("constant factor값을 입력해주세요 >> "))

        #processing
        roaster = make_roaster(name_arr, num, cf)

        #output
        print("\n<평일 당직표>", roaster)
    else:
        #input
        num = int(input("\n주말 당직 총 인원 수를 입력해주세요 >> "))
        name_arr = []
        for j in range(num):
            name_arr.append(input("%d번째 사람 이름을 입력해주세요 >> "%(j+1)))
        cf = int(input("constant factor값을 입력해주세요 >> "))

        #processing
        roaster = make_roaster(name_arr, num, cf)

        #output
        print("\n<주말 당직표>", roaster)