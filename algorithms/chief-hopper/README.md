Chief Hopper
=============

###Problem Statement

Chief's bot is playing an old DOS-based game. There are N+1 buildings in the game - indexed from 0 to N and are placed left-to-right. It is guaranteed that building with index 0 will be of height 0 unit. For buildings with index i (i ∈ [1,N]) height will be h<sub>i</sub> units. 

At beginning Chief's bot is at building with index 0. At each step, bot jumps to next (right) building. Suppose bot is at k<sup>th</sup> building and his current energy is botEnergy, then in next step he will jump to (k+1)<sup>th</sup> building. He will gain/lose energy equal in amount to difference between h<sub>k+1</sub> and botEnergy
* If h<sub>k+1</sub> > botEnergy, then he will lose h<sub>k+1</sub> − botEnergy units of energy.
* Otherwise, he will gain botEnergy − h<sub>k+1</sub> units of energy.
Goal is to reach N<sup>th</sup> building, and during the course bot should never have negative energy units. What should be the minimum units of energy with which bot should start to successfully complete the game?

###Input Format

The first line contains integer N. Next line contains N space separated integers h<sub>1</sub>,h<sub>2</sub>, ⋯,h<sub>N</sub> representing the heights of the buildings.

###Output Format

Print a single number representing minimum units of energy required to complete the game.

###Constraints 
* 1≤ N ≤10<sup>5</sup>
* 1≤ h<sub>i</sub> ≤10<sup>5</sup>,i∈[1,N]

###Sample Input
```
5
3 4 3 2 4
```
Sample Output
```
4
```
###Sample Input
```
3
4 4 4
```
###Sample Output
```
4
```
###Explanation

**Sample 1**
If initial energy is 4, after step 1 energy is 5, after step 2 it's 6, after step 3 it's 9 and after step 4 it's 16, finally at step 5 it's 28. 
You can verify for lower initial energy bot will have -ve energy in the end.

**Sample 2**
In the second test case if bot has energy 4, it's energy is changed by (4 - 4 = 0) at every step 