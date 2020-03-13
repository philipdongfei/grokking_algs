word_a = ['b','l','u','e']
word_b = ['c','l','u','e','s']
cell = [[]]*5
for a in range(0,5):
    cell[a].append(0)

def LCS(word_a, word_b, cell):
    for j in range(0,len(word_b)):
        for i in range(0,len(word_a)):
            print("i=",i)
            print("j=",j)
            if word_a[i] == word_b[j]:
                if (i-1)<0 | (j-1)<0:
                    cell[i][j] = 0 + 1
                else:
                    cell[i][j] = cell[i-1][j-1] + 1
            else:
                if i-1 < 0:
                    top = 0
                else:
                    top = cell[i-1][j]
                if j-1 < 0:
                    left = 0
                else:
                    left = cell[i][j-1]
                cell[i][j] = max(top, left)
    print(cell)

