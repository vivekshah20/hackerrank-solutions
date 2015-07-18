programs = ['C', 'CPP', 'JAVA', 'PYTHON', 'PERL', 'PHP', 'RUBY', 'CSHARP', 'HASKELL','CLOJURE', 'BASH', 'SCALA', 'ERLANG', 'CLISP', 'LUA', 'BRAINFUCK', 'JAVASCRIPT','GO', 'D', 'OCAML', 'R', 'PASCAL', 'SBCL', 'DART', 'GROOVY', 'OBJECTIVEC']
t = input()
for i in xrange(t):
    language = raw_input().strip().split()
    print "VALID" if language[1] in programs else "INVALID"