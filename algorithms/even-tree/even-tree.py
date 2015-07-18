# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, raw_input().split())
edges = []
for x in xrange(m):
    u, v = map(int, raw_input().split())
    edges.append([u, v])

inf = []

def findChildren(k):
    children = []
    for x in xrange(m):
        if edges[x][1] == k:
            children.append(edges[x][0])
            childN = findChildren(edges[x][0])
            for child in childN:
                children.append(child)
    return children
tree = []
def generateTree():
    global tree
    for x in xrange(n):
		tree.append([x+1])
    for x in xrange(n):
		tree[x].append(findChildren(x+1))
    return tree

generateTree()

count = 0
for x in xrange(n):
    if len(tree[x][1]) % 2 == 1:
        count += 1
print count - 1