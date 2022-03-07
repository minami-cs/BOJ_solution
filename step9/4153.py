while True:
    triangle = list(map(int, input().split()))
    if sum(triangle) == 0:
        break
    a = max(triangle)
    triangle.remove(a)
    if triangle[0]**2 + triangle[1]**2 == a**2:
        print('right')
    else:
        print('wrong')