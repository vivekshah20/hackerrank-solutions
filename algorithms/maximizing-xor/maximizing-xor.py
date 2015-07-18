
def  maxXor( l,  r):
    maxi =0
    for i in range(l,r+1):
        for j in range (i,r+1):
            if i^j>maxi:
                maxi=i^j
    return maxi
    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)