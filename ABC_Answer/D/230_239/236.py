# Qiitaの記事参照


# pypyで提出

# 再起回数上限を10^6へ変更
import sys
sys.setrecursionlimit(10**6)

# 入力の受け取り
N=int(input())

# 「相性」の表
A=[[0]*(2*N+1) for i in range(2*N+1)]

# i=1~(2N-1)
for i in range(1,2*N):
    # 入力を受け取る
    tmp=list(map(int,input().split()))
    # 表に記載
    for j in range(len(tmp)):
        A[i][j+(i+1)]=tmp[j]
        A[j+(i+1)][i]=tmp[j]

# 答え
ans=0

# 引数：selected(すでに選ばれている人)　pairs(ペアの一覧)
def DFS(selected,pairs):
    # ansを更新できるように
    global ans

    # 全員ペアができていれば
    # ⇔pairsの長さが2Nならば
    if len(pairs)==2*N:
        # 「楽しさ」の計算
        score=0
        # i=0~(2N-1)まで　2毎に増加
        for i in range(0,2*N,2):
            # ペアになる人
            x=pairs[i]
            y=pairs[i+1]
            # 「相性」から「楽しさ」を計算
            score^=A[x][y]
        
        # 「楽しさ」が大きかったら答えを更新
        ans=max(ans,score)

    # 次に追加する人が偶数番目
    # ⇔pairsの長さが偶数
    elif len(pairs)%2==0:
        # 選ばれていない中で一番小さい番号の人を選ぶ
        i=1
        while selected[i]==True:
            i+=1
        # pairsへ追加
        pairs.append(i)
        # 選択済みにする
        selected[i]=True
        # 次のDFSへ
        DFS(selected,pairs)
        # 前のDFSが終わったらpairsから消す
        pairs.pop()        
        # selectedをFalseへ変更
        selected[i]=False


    # 次に追加する人が奇数番目
    # ⇔pairsの長さが奇数
    else:
        # 選ばれていない人を一人ずつ全て選ぶ
        for i in range(1,2*N+1):
            # まだ選ばれていないなら
            if selected[i]==False:
                # 追加
                pairs.append(i)
                # 選択済みにする
                selected[i]=True
                # 次のDFSへ
                DFS(selected,pairs)
                # 前のDFSが終わったらpairsから消す
                pairs.pop()        
                # selectedをFalseへ変更
                selected[i]=False

# すでに選ばれているか(pairsの中に入っているか)管理するリスト
# =Falseなら選ばれていない、Trueならすでに選ばれている
# 最初は誰も選ばれていない
selected=[False]*(2*N+1)

# ペアになる人を記録するリスト(最初は空)
# 最終的にpairsの(0番目と1番目),(2番目と3番目),...,((2N-2)番目と(2N-1))をペアとする
pairs=[]

# DFSを開始
DFS(selected,pairs)

# 答えの出力
print(ans)