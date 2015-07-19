def insertionSort(ar):    
    for j in range(1, len(ar)):
        for i in reversed(range(j)):
            if ar[i + 1] < ar[i]:
                ar[i], ar[i + 1] = ar[i + 1], ar[i]
            else:
                break
            
        print ' '.join(map(str,ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)