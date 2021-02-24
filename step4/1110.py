n = int(input())
temp = n
count = 0
while True:
    ten = temp//10
    one = temp%10
    newtemp = ten+one
    newone = newtemp%10
    temp = one*10+newone
    count += 1
    if n == temp:
        break
print(count)