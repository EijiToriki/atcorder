import collections
N = int(input())
nameList = [list(map(str, input().split())) for nameList in range(N)]

adanaCandidate = []

for name in nameList:
  adanaCandidate.append(name[0])
  adanaCandidate.append(name[1])

## 重複したあだ名
doubleNameList = [k for k, v in collections.Counter(adanaCandidate).items() if v > 1]

result = "Yes"
sameSeiMei = []

for name in nameList:
  if name[0] != name[1]:    ## 1回提出後追記：姓名同じ人を考慮しなければならない
    if name[0] in doubleNameList and name[1] in doubleNameList:
      result = "No"
      break
  else:
    if name[0] in sameSeiMei:
      result = "No"
      break
    else:
      sameSeiMei.append(name[0])
  
print(result)