
t=input()
for x in range(0,t):
    n=input()
    a=input()
    b=input()
    solutions=[]
    for i in range(0,n):
        solutions.append(a*i+b*(n-i-1))
    solutions = set(solutions)
    print ' '.join(map(str,sorted(solutions)))