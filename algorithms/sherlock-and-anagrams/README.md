Sherlock and Anagrams
======================

###Problem Statement

Given a string **S**, find the number of unordered anagramic pairs of substrings.

###Input Format

First line contains **T**, the number of testcases. Each testcase consists of string **S** in one line.

###Constraints 
* 1≤T≤10 
* 2≤*length*(*S*)≤100 
* String S contains only the lowercase letters of the English alphabet.

###Output Format

For each testcase, print the required answer in one line.

###Sample Input
```
2
abba
abcd
```
###Sample Output
```
4
0
```
###Explanation

Let's say S[i,j] denotes the substring S<sub>i</sub>,S<sub>i+1</sub>,⋯,S<sub>j</sub>.

testcase 1: 
For S=`abba`, anagramic pairs are: **{S[1,1],S[4,4]}**, **{S[1,2],S[3,4]}**, **{S[2,2],S[3,3]}** and **{S[1,3],S[2,4]}**.

testcase 2: 
No anagramic pairs.