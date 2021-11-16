# Input

standardCode = input("기준 악보 >> ")
standardSimilarity = int(input("기준 유사도(%) >> "))
codeNum = int(input("입력할 악보 개수 >> "))

codes = []
for i in range(codeNum):
    codes.append(input("%d번째 악보 입력 >> "%(i+1)))


# Processing
# LCS (Longest Common Subsequence)
def LCS(n, x, y):
    C = [[0]*(n+1) for i in range(n+1)]   #이차원 배열 C 선언
    for a in range(n):
        for b in range(n):
            if x[a] == y[b]:
                C[a+1][b+1] = C[a][b] + 1
            else:
                C[a+1][b+1] = max(C[a][b+1], C[a+1][b])
    return C[n][n]

standardLength = round(len(standardCode) * standardSimilarity / 100.0)

similarCodes = {}
for code in codes:
    length = LCS(len(standardCode), standardCode, code)
    if length >= standardLength:
        similarCodes[code] = length


# OutPut

print("=====akbo list=====")
for code in similarCodes:
    print(code, "(similar:%d/%d)"%(similarCodes[code], len(standardCode)))
print("===================")