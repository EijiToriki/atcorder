from collections import defaultdict

N = int(input())
C = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    C[a] += 1  # a日目に1人増えます
    C[a + b] -= 1  # a + b 日目に1人減ります

ans = [0] * (N + 1)  # ans[i]: ちょうどi人がログインしていた日数
days = sorted(C.keys())  # 人数が変化する日のリストを昇順
prev_day = 0  # 前回人数が変化した日
cnt = 0   # ログインしている人数
for cur_day in days:
  ans[cnt] += cur_day - prev_day
  cnt += C[cur_day]
  prev_day = cur_day

print(*ans[1:])