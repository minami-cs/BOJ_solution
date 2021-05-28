word = input()

sum = 0
for i in range(len(word)):
    sum += 1
    if word[i] == '-' or word[i] == '=':
        sum -= 1
        if word[i-2] == 'd' and word[i-1] == 'z':
            sum -= 1
    if (word[i-1] == 'l' or word[i-1] == 'n') and word[i] == 'j':
        sum -= 1
print(sum)
