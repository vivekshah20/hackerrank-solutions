l=raw_input()
string = list(raw_input())
n = int(raw_input())
n = n%26
string1=""
for a in string:
    a = ord(a)
    if (a>96 and a<(123-n)) or (a>64 and a<(91-n)):
        a=chr(a+n)
        string1+=a
    elif (a in range(123-n,123)) or (a in range(91-n,91)) :
        a=chr(a-26+n)
        string1+=a
    else:
        a=chr(a)
        string1+=a
print string1