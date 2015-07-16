from __future__ import division
a = int(raw_input())
b = map(int, raw_input().strip().split(" "))
nc=pc=ec=0
for i in b:
    if i<0:
        nc+=1
    elif i>0:
        pc+=1
    else:
        ec+=1    
t=len(b)
print pc/t,"\n",nc/t,"\n",ec/t