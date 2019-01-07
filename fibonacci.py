# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:58:32 2019

models the reproductive rate of rabbits using the fibonacci sequence but with a twist
takes n to be the number of months they will be allowed to breed
takes k to be the number of rabbit pairs in each litter
starts with 1 rabbit pair

@author: Dr.C
"""

def fibonacci(n,k):
    f1 = 1  #initializes to 0 
    f2 = 1  #start with 1 pair
    if n<=2:
        return 1
    for i in range(2,n): #runs loop n times
        f  = (k*f1) + f2 #computes next value of the sequence
        f1 = f2  #sets to previous value 
        f2 = f

    return f2
