# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_index(string,subs):
    index=0
    c = subs[0]
    for ch in string:
        if ch==c:
            if string[index:index+len(subs)] == subs:
                    return index
        index+=1

def search_pattern(mat1,mat2,m):
    n=0
    i=0
    first = True
    a=[]
    for each in mat1:
        if n==m:
            break
        i+=1
        subs = ''.join(mat2[n])
        string = ''.join(each)

        if subs in string and (first or i ==n):
            index = get_index(string,subs)
            a.append(index)
            n+=1
            if first:
                first = False
                i=0
        if subs not in string and n>0:
            n=0
            first = True
            a=[]
    if n==m and len(set(a)) ==1:
        return "YES"
    else:
        return "NO"

t =input()
for i in range(0,t):
    m,n = map(int, raw_input().split())
    mat1 = []
    mat2 = []
    for j in range(0,m):
        x = list(raw_input().strip().split())
        mat1.append(x)
    m,n = map(int, raw_input().split())
    for j in range(0,m):
        x = list(raw_input().strip().split())
        mat2.append(x)
    ans = search_pattern(mat1,mat2,m)
    print ans