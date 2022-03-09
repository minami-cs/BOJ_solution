import math

t = int(input())
for n in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  r = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
  if r == 0 and r1 == r2:
    print(-1)
  elif r1 + r2 == r or math.sqrt((r1 - r2)**2) == r:
    print(1)
  elif math.sqrt((r1 - r2)**2) < r and r < (r1 + r2):
    print(2)
  else:
    print(0)
