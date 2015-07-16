def check_mkaprekar(num):
    sqr_num = str(num**2)
    left_num= int("0"+sqr_num[:len(sqr_num)//2])
    right_num = int("0"+sqr_num[len(sqr_num)//2:])
    if num == left_num+right_num:
        return True
p=input()
q=input()
for i in range(p,q):
    if check_mkaprekar(i):
        print i,