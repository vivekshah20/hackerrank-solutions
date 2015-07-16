A Very Big Sum
===============

###Problem Statement

You are given an array of integers of size ***N***. You need to print the sum of the elements of the array.

Note: A signed 32-bit integer value uses 1st bit to represent the sign of the number and remaining 31 bits to represent the magnitude. The range of the 32-bit integer is **−2<sup>31</sup> to 2<sup>31</sup>−1** *or* **[−2147483648,2147483647]**. When we add several integer values, the resulting sum might exceed this range. You might need to use long long int in C/C++ or long data type in Java to store such sums.

###Input Format

The first line of the input consists of an integer *N*. The next lines contain *N* space separated integers describing the array.

Constraints 
**1≤N≤10**
**0≤A[i]≤1010**

###Output Format

Output a single value equal to the sum of the elements of the array.

###Sample Input
```
5
1000000001 1000000002 1000000003 1000000004 1000000005
```
###Sample Output
```
5000000015
```