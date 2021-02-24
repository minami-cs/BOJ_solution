h = int(input())

for i in range(h):
    s = i + 1
    b = h - s
    for j in range(b):
        print(" ", end="")    
    print("*"*s)