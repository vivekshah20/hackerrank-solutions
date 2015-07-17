Funny String
=============

###Problem Statement

Suppose you have a string S which has length N and is indexed from 0 to N−1. String R is the reverse of the string S. The string S is funny if the condition |S<sub>i</sub>−S<sub>i−1</sub>|=|R<sub>i</sub>−R<sub>i−1</sub>| is true for every i from 1 to N−1.

(Note: Given a string str, str<sub>i</sub> denotes the ascii value of the i<sup>th</sup> character (0-indexed) of str. |x| denotes the absolute value of an integer x)

###Input Format

First line of the input will contain an integer T. T testcases follow. Each of the next T lines contains one string S.

###Constraints

* 1<=T<=10
* 2<=length of S<=10000

###Output Format

For each string, print `Funny` or `Not Funny` in separate lines.

###Sample Input
```
2
acxz
bcxz
```
###Sample Output
```
Funny
Not Funny
```
###Explanation

Consider the 1<sup>st</sup> testcase `acxz`

here

|c-a| = |x-z| = 2
|x-c| = |c-x| = 21
|z-x| = |a-c| = 2

Hence `Funny`.

Consider the 2<sup>nd</sup> testcase `bcxz`

here

|c-b| != |x-z|
Hence `Not Funny`.