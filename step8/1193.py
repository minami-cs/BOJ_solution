x = int(input())

# [1/1], [1/2, 2/1], [3/1, 2/2, 1/3], [1/4, 2/3, 3/2, 4/1], [5/1, 4/2, 3/3, 2/4, 1/5]
# 1       2          4                7                       11

line = 0
num = 0
denom = 0
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    num = x
    denom = line - x + 1
else:
    num = line - x + 1
    denom = x

print('%s/%s' % (num, denom))
