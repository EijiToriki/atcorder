## プログラミングの問題というよりかは，高校数学の問題
## 円の方程式と三角関数覚えているかな？？
import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    E = int(input())
    pointy = -(L/2)*math.sin(math.radians((360*E)/T))
    pointz = (L/2) -(L/2)*math.cos(math.radians((360*E)/T))

    edge_yz = pointz
    edge_xy = math.sqrt(X**2 + (pointy-Y)**2)

    ans = math.degrees(math.atan(edge_yz/edge_xy))
    print(ans)