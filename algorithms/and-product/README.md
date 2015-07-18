AND Product
===========
###Problem Statement

You will be given two integers A and B. You are required to compute the bitwise AND amongst all natural numbers lying between A and B, both inclusive.

###Input Format

First line of the input contains T, the number of testcases to follow. 
Each testcase in a newline contains A and B separated by a single space.

###Constraints

* 1≤T≤200 
* 0≤A≤B<232

###Output Format

Output one line per test case with the required bitwise AND.

###Sample Input
```
3 
12 15 
2 3 
8 13
```
###Sample Output
```
12 
2 
8
```
###Explanation

For the first testcase,

> 12 & 13 & 14 & 15 = 12

For second testcase,

> 2 & 3 = 2

For the third testcase,

> 8 & 9 & 10 & 11 & 12 & 13 = 8
