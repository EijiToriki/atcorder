import math


a,b,d = map(int, input().split())

ans_x = math.cos(math.radians(d)) * a - math.sin(math.radians(d)) * b
ans_y = math.sin(math.radians(d)) * a + math.cos(math.radians(d)) * b

print(*[ans_x, ans_y])