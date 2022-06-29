def makeDict(xlist):
    dic = {}
    for x in xlist:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    return dic

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

## 感心があるのは，あまりだけ
A = [a%46 for a in A]
B = [b%46 for b in B]
C = [c%46 for c in C]

## 0～45のあまりをカウントする辞書を作成
Adict = makeDict(A)
Bdict = makeDict(B)
Cdict = makeDict(C)

ans = 0
for kA, vA in Adict.items():
    for kB, vB in Bdict.items():
        for kC, vC in Cdict.items():
            if (kA + kB + kC) % 46 == 0:
                ans += (vA*vB*vC)

print(ans)