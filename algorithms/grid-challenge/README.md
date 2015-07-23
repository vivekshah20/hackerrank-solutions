Grid Challenge
===============

###Problem Statement

Given a squared sized grid *G* of size *N* in which each cell has a lowercase letter. Denote the character in the ith row and in the jth column as G[*i*][*j*].

You can perform one operation as many times as you like: Swap two column adjacent characters in the same row G[*i*][*j*] and G[*i*][*j+1*] for all valid i,j.

Is it possible to rearrange the grid such that the following condition is true?

G[i][1]≤G[i][2]≤⋯≤G[i][N] for 1≤i≤N and 
G[1][j]≤G[2][j]≤⋯≤G[N][j] for 1≤j≤N
In other words, is it possible to rearrange the grid such that every row and every column is lexicographically sorted?

**Note:** c<sub>1</sub> ≤ c<sub>2</sub>, if letter c<sub>1</sub> is equal to c<sub>2</sub> or is before c<sub>2</sub> in the alphabet.

###Input Format

The first line begins with T, the number of testcases. In each testcase you will be given N. The following N lines contain N lowercase english alphabet each, describing the grid.

###Output Format

Print T lines. On the ith line print `YES` if it is possible to rearrange the grid in the ith testcase or `NO` otherwise.

###Constraints 
* 1≤T≤100 
* 1≤N≤100 
* G<sub>ij</sub> will be a lower case letter

###Sample Input
```
1
5
ebacd
fghij
olmkn
trpqs
xywuv
```

###Sample Output
```
YES
```
###Explanation

The grid in the first and only testcase can be reordered to
```
abcde
fghij
klmno
pqrst
uvwxy
```
This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all lexicographically sorted.