print("")

trollList = []
while True:
    troll = input("필터링 대상 입력 (끝내고 싶으면 0을 입력) >> ")
    if troll == "0":
        break
    trollList.append(troll)

comment = list(input("댓글 입력 >> "))

count = 0
for troll in trollList:
    length = len(troll)
    for i in range(len(comment) - length + 1):
        j = 0
        while j < length and troll[j] == comment[i+j]:
            j += 1
        if j == length:
            count += 1
            for l in range(length):
                comment[i+l] = '*'
comment = "".join(comment)

if count >= 2:
    comment = "이 댓글은 가려졌습니다."

print("\n필터링 결과 >>", comment, "\n")