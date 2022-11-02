# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:21:33 2022

@author: Saleh Kehoul
"""
"Reset the global space"
%reset -f


"Open the triangle text file"
with open('triangle.txt') as solution:
    jaggedTriangle = [[int(i) for i in rows.split()] for rows in solution]

"""
Calculation of maximum sum algorithm:
    The algorithm first reads in the triangle data and "jags" it creating a 
    triangle shifted to the right. This will therefore make it possible to
    navigate the to the right and down. In any given iterative move, the 
    algorithm computes the sum of the two adjacent numbers to the previous sum
    and stores only the biggest of two. This renders the remaining data to the 
    left zero.
    The way this saves time is that in each row there will be only two 
    comparisons made between two sums and the largest is saved.
"""
previousSum = []
for row in jaggedTriangle:
    currentSums = []
    for p, valueAdj in enumerate(row):
        rightSum = 0 if p >= len(previousSum) else previousSum[p]
        leftSum = (previousSum[p - 1]
                         if 0 < p <= len(previousSum)
                         else 0)
        currentSums.append(max(rightSum, leftSum) + valueAdj)

    previousSum = currentSums

print('The maximum sum of the triangle is', max(previousSum))