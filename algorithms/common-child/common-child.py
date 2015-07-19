string1=raw_input()
string2=raw_input()

x = len(string1)
y = len(string2)

n = [[0 for _ in xrange(y+1)] for _ in xrange(x+1)]

for i in xrange(1, x+1):
    for j in xrange(1, y+1):
        if string1[i-1]==string2[j-1]:
            n[i][j] = n[i-1][j-1]+1
        elif n[i-1][j]>=n[i][j-1]:
            n[i][j]=n[i-1][j]
        else:
            n[i][j] = n[i][j-1]
print n[x][y]