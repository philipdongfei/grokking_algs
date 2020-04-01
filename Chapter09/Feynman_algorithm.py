# pseudocode

def longest_common_substring(word_a, word_b):
    n = len(word_a)+1
    m = len(word_b)+1
    #print("n=%d,m=%d" % (n, m))
    cell = [[0 for k in range(m)] for l in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if word_a[i-1] == word_b[j-1]:
                #print("%d,%d,%s" % (i-1,j-1,cell[i-1][j-1]))
                cell[i][j] = cell[i-1][j-1] + 1
                #print("%d,%d,%s" % (i,j,cell[i][j]))
                #print()
            else:
                #print("i=%d, j=%d" % (i,j))
                cell[i][j] = 0
    return max(max(values) for values in cell)

if __name__ == "__main__":
    word_a = "fish" #["f","i","s","h"]
    word_b = "hish" #["h","i","s","h"]
    word_c = "vista" #["v","i","s","t","a"]
    value = longest_common_substring(word_a,word_b)
    print("(%s, %s) = %d" % (word_a,word_b, value))
    value = longest_common_substring(word_b,word_c)
    print("(%s, %s) = %d" % (word_b,word_c, value))


