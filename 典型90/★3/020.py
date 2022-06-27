## log で計算すると，小数の誤差で正しい答えが出てこない
## 普通に指数で計算する（pow関数は，値がオーバーフローするかもしれないからforで書く）

import sys

a, b, c = map(int, input().split())

c_b = 1

for _ in range(b):
    c_b *= c
    if a < c_b:
        print('Yes')
        sys.exit()
        
print('No')