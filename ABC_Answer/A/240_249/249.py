A, B, C, D, E, F, X = map(int, input().split())

loopTimeT = (X // (A + C)) * A
amariTimeT = X - (X // (A + C)) * (A + C)
if amariTimeT >= A:
  amariTimeT = A
totalTimeT = loopTimeT + amariTimeT

disT = B * totalTimeT

loopTimeA = (X // (D + F)) * D
amariTimeA = X - (X // (D + F)) * (D + F)
if amariTimeA >= D:
  amariTimeA = D
totalTimeA = loopTimeA + amariTimeA

disA = E * totalTimeA

if disT > disA:
  print("Takahashi")
elif disT < disA:
  print("Aoki")
else:
  print("Draw")