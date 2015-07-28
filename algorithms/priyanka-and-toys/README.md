Priyanka and Toys
==================
###Problem Statement

Little Priyanka visited a kids' shop. There are N toys and their weight is represented by an array W=[w<sub>1</sub>,w<sub>2</sub>,…,w<sub>N</sub>]. Each toy costs 1 unit, and if she buys a toy with weight w′, then she can get all other toys whose weight lies between [w',w'+4] (both inclusive) free of cost.

###Input Format

The first line contains an integer N i.e. number of toys.
Next line will contain N integers, w<sub>1</sub>,w<sub>2</sub>,…,w<sub>N</sub>, representing the weight array.

###Output Format

Minimum units with which Priyanka could buy all of toys.

###Constraints 
* 1 ≤ N ≤10<sup>5</sup>
* 0 ≤ w<sub>i</sub>≤ 10<sup>4</sup>, where i∈[1,N]

###Sample Input
```
5
1 2 3 17 10
```
###Sample Output
```
3
```
###Explanation

She buys 1<sup>st</sup> toy with weight 1 for 1 unit and gets 2<sup>nd</sup> and 3<sup>rd</sup> toy for free since their weight lies between [1,5]. And she has to buy last two toys separately.