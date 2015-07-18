import re,sys
n =input()
string = sys.stdin.read()
regex=re.compile(r"[\w+-]+(?:\.[\w+-]+)*@[\w+-]+(?:\.[\w+-]+)*(?:\.[a-zA-Z]{2,4})")
t=regex.findall(string) 
t=list(set(t))
t.sort()
print ';'.join(t)