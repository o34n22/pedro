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

#def make_search_list(target=1999):
#    """
#    these lists should be written to file at some point
#    (only ~ 20 different ones exist)
#    """
#    L0 = list(range(10))
#    L = []
#    target_length = len(str(target))
#    print(target_length)
#    target_rounded = round(target,-target_length+1)
#    print(target_rounded)
#    d = int(str(target_rounded)[0])
#    print("d = " + str(d))
#    if target_rounded - target > 0: 
#        d -= 1
#        while len(L) != 10:
#            print("d = " + str(d))
#            L.append(L0.pop(d))
#            L.append(L0.pop(d))
#            print(L0)
#            print(L)
#            if d != 0:
#                d -= 1
#        return L
#    else:
#        while len(L) != 10:
#            L.append(L0.pop(d))
#            if d != 0:
#                d -= 1
#            L.append(L0.pop(d))
#        return L

def get_search_list(target=1999):
    filename = 'search_lists.csv'
    with open(filename) as f:
        L = np.loadtxt(f,dtype=int,delimiter=' ')
    t = int(str(target)[:2])
    line_index = ceil(0.2*t) 
    return L[line_index]
    
#def tail(n, R2, target=5472):
#    n = str(n)
#    for i in range(len(R2)):
#        R2[i] = int(R2[i])        
#    list.sort(R2)
#    S = []
#    # -------
#    N = [int(d) for d in n]
#    N.pop(N.index(R2[0]))
#    N.sort(reverse=True)
#    N = [R2[0]] + N
#    s = ''
#    for d in N:
#        s += str(d)
#    S.append(int(s))
#    # -------
#    N = [int(d) for d in n]
#    N.pop(N.index(R2[1]))
#    N.sort(reverse=False)
#    N = [R2[1]] + N
#    s = ''
#    for d in N:
#        s += str(d)
#    S.append(int(s))
#    # ------- distance to target
#    S_ = S.copy()
#    for i in range(len(S)):
#        S_[i] -= target
#        S_[i] = abs(S_[i])
#    if S_[0] != S_[1]:
#        min_index = min(range(len(S)),key=S_.__getitem__)
#        return S[min_index]
#    pass # catch case of two nearest permutations here
    
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
    n = str(n)
    if int(n) == target:
        return n
    if len(n) == 2:
        """only two digits left -> direct comparison"""
        distance_1 = abs(int(n) - target)
        distance_2 = abs(int(n[1]+n[0]) - target)
        if distance_1 < distance_2:
            return n
        else:
            return n[1] + n[0]
    A = get_search_list(target=target)
    print('A: ',A)
    i = 0 # index in search list
#    print("searching n = " + n)
    b = n.find(str(A[i]))
    if b != -1:
        inner0 = n[b]
#        print(b)
        print("found a " + inner0 + " at position " + str(b))
        i += 1
        c = n.find(str(A[i]))
        outer0 = '-1'
        if c != -1:
            outer0 = n[c]
            print("found a " + outer0 + " at position " + str(c))
        else:
            print("found no " + str(A[i]))
            new_n = n[:b]+n[(b+1):]
            t = int(str(target)[1:])
            print("target = " + str(target) + " ...new target = " + str(t))
            print("     n = " + n + " ...new n =      " + str(new_n))
            inner = inner0 + solve_0(new_n,target=t)
        if int(outer0) != -1 and int(outer0) < A[0]:
            outer = outer0 + tail(n[:c]+n[(c+1):],True)
        else:
            outer = outer0 + tail(n[:c]+n[(c+1):],False)
        print("outer: "+ str(outer))
        out_distance = abs(int(outer) - target)
        t = int(str(target)[1:])
        print("target = " + str(target) + " ...new target = " + str(t))
        new_n = n[:b]+n[(b+1):]
        print("     n = " + n + " ...new n =      " + str(new_n))
        print("inner again")
        inner = inner0 + solve_0(new_n,target=t)
#        print("inner: " + str(inner))
        in_distance = abs(int(inner) - target)
        if out_distance < in_distance:
            return outer
        else:
            return inner
    else:
        print("hello from out here")
        i += 1
        """if I didn't find i=0 search for two outers and compare directly"""
        while b == -1:
            b = n.find(str(A[i]))
            if b != -1:
                outer0 = n[b]
                if int(outer0) < A[0]:
                    outer_1 = outer0 + tail(n[:b]+n[(b+1):],True)
                else:
                    outer_1 = outer0 + tail(n[:b]+n[(b+1):],False)
                i += 1
                b = n.find(str(A[i]))
                outer0 = n[b]
                if int(outer0) < A[0]:
                    outer_2 = outer0 + tail(n[:b]+n[(b+1):],True)
                else:
                    outer_2 = outer0 + tail(n[:b]+n[(b+1):],False)
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


#k = 0
##L = [910,956,249,847,123]
#while k < 10:
#    number = rd.randint(1000,9999)
##    number = L[k]
#    print('number: '+str(number))
#    print(int(solve(number)))
#    print(solve_0(number))
#    k += 1
example_n = 2062
print("number: " + str(example_n))
print("correct solution:   " + solve(example_n))
print("suggested solution: " + solve_0(example_n))

#print(get_search_list(target=999))
