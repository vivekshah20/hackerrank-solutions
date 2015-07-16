Plus Minus
==========

###Problem Statement

You're given an array containing integer values. You need to print the fraction of count of positive numbers, negative numbers and zeroes to the total numbers. Print the value of the fractions correct to 3 decimal places.

###Input Format

First line contains *N*, which is the size of the array. 
Next line contains *N* integers **A<sub>1</sub>,A<sub>2</sub>,A<sub>3</sub>,⋯,A<sub>N</sub>**, separated by space.

###Constraints 
* `1≤N≤100` 
* `−100≤A<sub>i</sub>≤100`

###Output Format

Output three values on different lines equal to the fraction of count of positive numbers, negative numbers and zeroes to the total numbers respectively correct to 3 decimal places.

###Sample Input
```
6
-4 3 -9 0 4 1          
```
###Sample Output
```
0.500
0.333
0.167
```
###Explanation

There are 3 positive numbers, 2 negative numbers and 1 zero in the array. 
Fraction of the positive numbers, negative numbers and zeroes are 3/6= *0.500*, 2/6= *0.333* and 1/6= *0.167* respectively.

**Note** This challenge introduces precision problems. You can even print output to 4 decimal places and above but only the difference at 3rd decimal digit is noted. That is the reason you'll notice testcases have much higher precision (more decimal places) than required. 
Answers with absolute error upto **10<sup>−4</sup>** will be accepted.