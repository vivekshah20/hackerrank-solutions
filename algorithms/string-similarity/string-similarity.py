def stringSimilarity(a):
    # Solved using Z Algorithm : http://codeforces.com/blog/entry/3107
    n = len(a)
    z = [0]*n
    l=r=0
    for i in range(1,n):
        if (i<=r):
            z[i]=min (r - i + 1, z[i - l])
        while(i + z[i] < n and a[z[i]] == a[i + z[i]]):
            z[i]+=1
        if (i + z[i] - 1 > r):
            l = i 
            r = i + z[i] - 1
    return sum(z)+n

if __name__ == '__main__':
    t = input()
    for i in range(0,t):
        a=raw_input()
        print stringSimilarity(a)