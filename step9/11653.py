# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51,....
n = int(input())
soinsu = 2

while n != 1:
    if n % soinsu == 0:
        n /= soinsu
        print(soinsu)
    else:
        soinsu += 1
