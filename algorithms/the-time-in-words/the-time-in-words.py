

n = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
    23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty seven',
    28: 'twenty eight', 29: 'twenty nine'
}

h = input()
m = input()

if m == 0:
    print(n[h] +' o\' clock')
elif m == 15:
    print('quarter past '+ n[h])
elif m < 30:
    print(n[m] +' minutes past '+ n[h])
elif m == 30:
    print('half past '+ n[h])
elif m == 45:
    print('quarter to '+ n[(h + 1) % 12])
else:
    print(n[60 - m] +' minutes to '+ n[(h + 1) % 12])