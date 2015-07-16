import math
s = raw_input()
rows = int(math.floor(math.sqrt(len(s))))
cols = int(math.ceil(math.sqrt(len(s))))

while (len(s)> rows*cols):
    rows = int(math.ceil(math.sqrt(len(s))))
final =[]
count=0
for i in xrange(0,rows):
    a =[]
    for j in range(0,cols):
        if count<len(s):
            a.extend(s[count])
            count+=1
    final.append(a)
string=""    
for i in xrange(0,cols):
    for j in xrange(0,rows):
        try:
            string+= final[j][i]
        except:
            continue
    string+=" "
print string