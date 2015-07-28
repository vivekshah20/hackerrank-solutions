Largest Permutation
===================

###Problem Statement

You are given an array of N integers which is a permutation of the first N natural numbers. You can swap any two elements of the array. You can make at most K swaps. What is the largest permutation, in numerical order, you can make?

###Input Format 
The first line of the input contains two integers, N and K, the size of the input array and the maximum swaps you can make, respectively. The second line of the input contains a permutation of the first N natural numbers.

###Output Format 
Print the lexicographically largest permutation you can make with **at most *K*** swaps.

###Constraints 
* 1≤ N ≤10<sup>5</sup> 
* 1≤ K ≤10<sup>9</sup>

###Sample Input#00
```
5 1
4 2 3 5 1
```
###Sample Output#00
```
5 2 3 4 1
```
###Explanation#00 

You can swap any two numbers in [4,2,3,5,1] and see the largest permutation is [5,2,3,4,1]

###Sample Input#01
```
3 1
2 1 3
```
###Sample Output#01
```
3 1 2
```

###Explanation#01 
With 1 swap we can get [1,2,3], [3,1,2] and [2,3,1] out of these [3,1,2] is the largest permutation.

###Sample Input#02
```
2 1
2 1
```
###Sample Output#02
```
2 1
```
Explanation#02 
We can see that [2,1] is already the largest permutation. So we don't need any swaps.