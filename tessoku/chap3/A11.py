from bisect import bisect

## 二分探索ハードコーティング
def my_binary_search(n, x, num_list):
  l = 0
  r = n
  while l < r:
    mid = (l + r) // 2
    if num_list[mid] < x:
      l = mid
    elif num_list[mid] > x:
      r = mid
    else:
      return mid


## 二分探索ライブラリ使用(bisect)
def library_binary_search(x, num_list):
  return bisect(num_list, x)


N, X = map(int, input().split())
A = list(map(int, input().split()))

# ans = my_binary_search(N, X, A) + 1
ans = library_binary_search(X, A)

print(ans)
