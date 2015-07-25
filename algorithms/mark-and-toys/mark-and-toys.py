def max_toys(prices, rupees):
    prices = sorted(prices)
    s=ret=0
    for i in prices:
        s+=i
        if s>=rupees:
            break
        ret+=1
    return ret
    
if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)