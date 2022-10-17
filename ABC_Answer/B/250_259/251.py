import itertools

N, W = map(int, input().split())
A = list(map(int, input().split()))+[0,0]

goodNum = []

if len(A) >= 3:
  for pair in itertools.combinations(A, 3):
    if sum(pair) <= W:
      goodNum.append(sum(pair))     

print(len(set(goodNum)))