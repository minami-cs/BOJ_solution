w = str(input()).upper()
temp = list(set(w))
nums = []
for i in temp:
    cnt = w.count(i)
    nums.append(cnt)
count = 0
for i in nums:
    if max(nums) == i:
        count += 1
if count == 1:
    n = nums.index(max(nums))
    print(temp[n])
else:
    print('?')
