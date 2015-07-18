__author__ ='Vivek Shah'
def insertionSort(ar):    
    if len(ar) == 1:
        print(' '.join(map(str, ar)))
    else:
        m = ar[-1]
        
        for i in reversed(range(len(ar) - 1)):
            if m < ar[i]:
                ar[i + 1] = ar[i]
                print(' '.join(map(str, ar)))
                
                if i == 0:
                    ar[0] = m
                    print(' '.join(map(str, ar)))
                    break
            else:
                ar[i + 1] = m
                print(' '.join(map(str, ar)))
                break

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)