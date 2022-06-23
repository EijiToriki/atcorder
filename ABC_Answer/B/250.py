N, A, B = map(int, input().split())

start_str = "."

for i in range(N*A):
    row_result = ""
    if i != 0:
      if i % A == 0 and start_str == ".":
        start_str = "#"
      elif i % A == 0 and start_str == "#":
        start_str = "."
    
    for j in range(N*B):
      if j==0:
        add_str = start_str
      else:
        if j % B == 0 and add_str == ".":
          add_str = "#"
        elif j % B == 0 and add_str == "#":
          add_str = "."
        
      row_result = row_result + add_str
    print(row_result)