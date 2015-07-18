n = input()
sentences=""
for i in xrange(n):
    sentences+=raw_input()+" "
t = input()
for i in xrange(t):
    word = raw_input()
    bword = word[:len(word)-2]+"se"
    print (sentences.count(word)+sentences.count(bword))