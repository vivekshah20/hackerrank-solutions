"""Using Turan Graph's Algorithm
    The number of edges is defined by the formula given below""" 

def Turan(n, r):
    return 0.5*(n**2-(n%r)*(n/r+1)**2-(r-(n%r))*(n/r)**2)


t = input()
for t in xrange(t):
    N,M = map(int, raw_input().split(' '))
    low,high=0,N
    while low+1<high:
        mid=(low+high)/2
        r=Turan(N,mid)
        
        if r<M:
            low=mid
        else:
            high=mid
    
    print high