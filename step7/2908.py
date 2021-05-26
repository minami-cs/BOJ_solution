a, b = input().split()
l = []
for i in a:
    l.append(i)
for i in b:
    l.append(i)
rl = l.reverse()
ra = ''
rb = ''
for i in range(len(l)):
    if i < 3:
        ra += l[i]
    else:
        rb += l[i]
if int(ra) > int(rb):
    print(ra)
else:
    print(rb)
