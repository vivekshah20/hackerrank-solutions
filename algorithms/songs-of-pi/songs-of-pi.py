a = int(raw_input())
b="31415926535897932384626433833"
b = list(map(int,b))

for i in range(0,a):
    song = list(raw_input().strip().split(" "))
    length = len(song)
    count=0
    for each in range(0,length):
        if (len(song[each])==b[each]):
            count+=1
    if count == length:
        print "It's a pi song."
    else:
        print "It's not a pi song."