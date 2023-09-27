class AtCoderMarketItem:
  def __init__(self, price, func_cnt, func_set):
    self.price = price
    self.func_cnt = func_cnt
    self.func_set = func_set

  def getPrice(self):
    return self.price

  def getFuncCnt(self):
    return self.func_cnt
  
  def getFuncSet(self):
    return self.func_set

def is_expensive(Pi, Pj):
  if Pi >= Pj:
    return True
  else:
    return False

def has_func_i(i_func_set, j_func_set):
  return i_func_set.issubset(j_func_set)

def is_superior(Pi, Pj, func_cnt_i, func_cnt_j):
  if Pi > Pj or func_cnt_j > func_cnt_i:
    return True
  else:
    return False


N, M = map(int, input().split())
items = []
for _ in range(N):
  PCF = list(map(int, input().split()))
  price, func_cnt, func_set = PCF[0], PCF[1], set(PCF[2:])
  item = AtCoderMarketItem(price, func_cnt, func_set)
  items.append(item)

for i in range(N):
  for j in range(N):
    i_price, j_price = items[i].getPrice(), items[j].getPrice()
    i_func_cnt, j_func_cnt = items[i].getFuncCnt(), items[j].getFuncCnt()
    i_func_set, j_func_set = items[i].getFuncSet(), items[j].getFuncSet()
    if is_expensive(i_price, j_price) and has_func_i(i_func_set, j_func_set) and is_superior(i_price, j_price, i_func_cnt, j_func_cnt):
      print('Yes')
      exit()
print('No')
