wn = str(input())
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0

for i in wn:
    for j in range(len(alphabet)):
        for k in range(len(alphabet[j])):
            if i == alphabet[j][k]:
                sum += (alphabet.index(alphabet[j]) + 3)

print(sum)
