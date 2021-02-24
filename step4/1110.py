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

#참고:https://gabii.tistory.com/entry/BaekJoonPython3-%EB%B0%B1%EC%A4%80-1110%EB%B2%88-%EB%8D%94%ED%95%98%EA%B8%B0-%EC%82%AC%EC%9D%B4%ED%81%B4