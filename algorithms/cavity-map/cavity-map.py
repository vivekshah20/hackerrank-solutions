t = input()
num = [list(map(int,raw_input())) for _ in range(t)]
for i in range(1,t-1):
    for j in range (1,t-1):
        if (num[i][j]>num[i][j+1] and num[i][j]>num[i][j-1] and num[i][j]>num[i+1][j] and num[i][j]>num[i-1][j]):
            num[i][j]='X'

for i in num:
	print ''.join(map(str,i))