
num1, num2 = map(int,raw_input().split())
team = [raw_input() for j in range(num1)]

count=maxi=0
max_count=1
for i,j in enumerate(team):
    for m,n in enumerate(team[i:]):
        count = bin(int(j,2)|int(n,2)).count('1')
        
        if (count==maxi):
            max_count+=1
        elif count> maxi:
            maxi=count
            max_count=1
        
print maxi,"\n",max_count