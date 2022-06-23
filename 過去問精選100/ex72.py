## 逆元を使って，nCr を求める
## Pythonで実行する

def pre_nCk(N,P):
  fact = [1 for _ in range(N+1)]
  fact_inv = [0 for _ in range(N+1)]
  fact_inv[0] = 1
  fact_inv[1] = 1

  for i in range(2,N+1):
    fact[i] = fact[i - 1] * i % P
    fact_inv[i] = fact_inv[i - 1] * pow(i, -1, P) % P
  
  return fact, fact_inv

def nCk(fact, fact_inv, n, k, P):
  return fact[n] * (fact_inv[k] * fact_inv[n-k] % P) % P

def main():
  W, H = map(int, input().split())
  N = W + H - 2
  P = 10**9 + 7

  fact, fact_inv = pre_nCk(N,P)
  result = nCk(fact, fact_inv, N, W-1, P)
  
  print(result)

if __name__ == "__main__" :
  main()
