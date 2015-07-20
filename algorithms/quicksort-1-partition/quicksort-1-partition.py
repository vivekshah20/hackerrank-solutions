def partition(ar):    
    return [n for n in ar if n < ar[0]] + [n for n in ar if n >= ar[0]]

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print ' '.join(map(str,partition(ar)))