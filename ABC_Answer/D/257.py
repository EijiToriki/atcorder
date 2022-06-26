## Sを二部探索で発見する（S = mid）
## ジャンプ台の繋がりはグラフで考える．
## あるジャンプ台を始点としたとき，全てのジャンプ台を回れるかどうかは，BFSにより求める．
## 探索されていないノードがなければ，そのジャンプ台から全てのジャンプ台へ飛ぶことができることを表す

from queue import Queue

N = int(input())
xyp = [map(int, input().split()) for _ in range(N)]
X, Y, P = [list(i) for i in zip(*xyp)]

max_jump = max(P)
max_jump_index = P.index(max(P))

posi = 10**10
nega = 0

while posi - nega > 1:
    mid = (posi + nega) // 2
    G = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i!= j:
                if P[i]*mid >= abs(X[i] - X[j]) + abs(Y[i] - Y[j]):
                    G[i].append(j)

    search_flag = False
    for i in range(N):
        # 各頂点が何手目に探索されたか
        # -1 は「まだ探索されていない」ことを表す
        dist = [-1] * N

        # todo リストを表すキュー
        que = Queue()

        # 頂点 0 を始点とする
        dist[i] = 0
        que.put(i)

        # キューが空になるまで探索する
        while not que.empty():
            # キューから頂点を取り出す
            v = que.get()

            # 頂点 v から 1 手で行ける頂点 next_v を探索
            for next_v in G[v]:
                # 頂点 next_v が探索済みであれば何もしない
                if dist[next_v] != -1:
                    continue

                # 頂点 next_v を探索する
                dist[next_v] = dist[v] + 1
                que.put(next_v)  

        if -1 not in dist:
            search_flag = True
            break
    
    if search_flag:
        posi = mid
    else:
        nega = mid

print(posi)