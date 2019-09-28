#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
fix:
number with two nearest permutations?
"""

import random as rd
import numpy as np
from math import ceil

def permutations(n):
    """
    takes some integer n as a str or int
    produces list of all permutations
    """
    if type(n) == int: 
        n = str(n)
    digits = len(n)
    if digits == 0:
        return []
    elif digits == 1:
        return [n]
    else:
        L = [] 
        for i in range(digits): # gotta start from tail!
            for p in permutations(n[:i]+n[i+1:]):
                L.append(n[i] + p)
    return L

def is_permutation(n,m):
    """
    takes two integers n,m with same number of digits
    and returns True if n is a permuation of m
    """
    n, m = str(n), str(m)
    for i in n:
        b = n.find(m[0])
        if b == -1:
            return False
        m = m[1:]
        n = n[:b] + n[(b+1):]
    return True

def pose(target=1999):
    """
    returns str
    (a random integer with same number of digits as target number)
    """
    while True:
        digits = len(str(target))
        n = 0
        for position in range(digits):
            place_value = 10**position
            n += place_value*rd.randint(0,9)
        if len(str(n)) == digits: 
            return str(n)

# to-do: catch type errors

def solve(n,target=1999):
    """
    solves by computing all permutations and the corresponding
    distance to target
    number of permutations ~ len(n)!
    only for testing purposes
    do not use in production!
    """
    P = permutations(n)
    D = target*np.ones(len(P),dtype=int)
    j = 0
    j_min = 0
    for p in P:
        D[j] = abs(target - int(p))
        if D[j] < D[j_min]: j_min = j
        j+=1
    return P[j_min]


def get_search_list(target=1999):
    filename = 'search_lists.csv'
    with open(filename) as f:
        L = np.loadtxt(f,dtype=int,delimiter=' ')
    power = len(str(target)) - 1
    line_index = ceil(2*target*0.1**power)
    return L[line_index]
    
    
def tail(n_tail,below=True):
    N = [int(d) for d in n_tail]
    N.sort(reverse=below)
    s = ''
    for d in N:
        s += str(d)
    return s
    

def solve_0(n, target=1999):
    """
    aims to find the nearest number with the smallest number
    of comparisons needed
    """
    if int(n) == target:
        return n
    n = str(n)
    if len(n) == 2: # only two digits left -> direct comparison
        distance_1 = abs(int(n) - target)
        distance_2 = abs(int(n[1]+n[0]) - target)
        if distance_1 < distance_2:
            return n
        else:
            return n[1] + n[0]
    A = get_search_list(target=target)
    i = 0 # index in search list
    b = n.find(str(A[i]))
    if b != -1:
        inner0 = n[b]
        i += 1
        c = n.find(str(A[i]))
        outer0 = '-1'
        if c != -1:
            outer0 = n[c]
        else:
            new_n = n[:b]+n[(b+1):]
            t = int(str(target)[1:])
            inner = inner0 + solve_0(new_n,target=t)
            return inner
        if int(outer0) != -1 and int(outer0) < A[0]:
            outer = outer0 + tail(n[:c]+n[(c+1):],below=True)
        else:
            outer = outer0 + tail(n[:c]+n[(c+1):],below=False)
        out_distance = abs(int(outer) - target)
        t = int(str(target)[1:])
        new_n = n[:b]+n[(b+1):]
        inner = inner0 + solve_0(new_n,target=t)
        in_distance = abs(int(inner) - target)
        if out_distance < in_distance:
            return outer
        else:
            return inner
    else:
        i += 1
        while b == -1:
            b = n.find(str(A[i]))
            if b != -1:
                outer0 = n[b]
                if int(outer0) < A[0]:
                    outer_1 = outer0 + tail(n[:b]+n[(b+1):],below=True)
                else:
                    outer_1 = outer0 + tail(n[:b]+n[(b+1):],below=False)
                if i < 9:
                    i += 1
                b = n.find(str(A[i]))
                if b == -1:
                    return outer_1
                outer0 = n[b]
                if int(outer0) < A[0]:
                    outer_2 = outer0 + tail(n[:b]+n[(b+1):],below=True)
                else:
                    outer_2 = outer0 + tail(n[:b]+n[(b+1):],below=False)
                break
            i += 1
        distance_1 = abs(int(outer_1) - target)
        distance_2 = abs(int(outer_2) - target)
        if distance_1 < distance_2:
            return outer_1
        else:
            return outer_2
          

def wrong(n,ans):
    if is_permutation(n,ans):
        message = 'It seems there is a number yet nearer to 500.' # target!!!
    else:
        message = 'Digits aren\'t matching. You must use the digits from \
                  the number given.'
#    else:
#        message = "I\'m speechless."
    return message


# --------------- testing ----------------


k = 0
#L = [910,956,249,847,123]
while k < 10000:
    number = rd.randint(1000,9999)
#    number = L[k]
#    print('number: '+str(number))
#    print(int(solve(number)))
#    print(solve_0(number))
    bum = int(solve(number)) - int(solve_0(number))
    if bum != 0:
        print('shit!')
        print(number)
    k += 1
#example_n = 9999
#print("number: " + str(example_n))
#print("correct solution:   " + solve(example_n))
#print("suggested solution: " + solve_0(example_n))

#print(get_search_list(target=1999))
