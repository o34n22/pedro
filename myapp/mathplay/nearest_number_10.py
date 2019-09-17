#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
fix:
number with two nearest permutations?
"""

import random as rd
import numpy as np

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

#def pose(target=500):
#    """
#    returns str
#    (a random integer with same number of digits as target number)
#    """
#    while True:
#        digits = len(str(target))
#        n = 0
#        for position in range(digits):
#            place_value = 10**position
#            n += place_value*rd.randint(0,9)
#        if len(str(n)) == digits: 
#            return str(n)

# to-do: catch type errors

def solve(n,target=5472):
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

def make_this_list(target=5472):
    """
    these lists should be written to file at some point
    (only 20 different ones exist)
    """
    L0 = list(range(10))
    L = []
    target_length = len(str(target))
    target_rounded = round(target,-target_length+1)
    d = int(str(target_rounded)[0])
    if target_rounded - target > 0: 
        d -= 1
        while len(L) != 10:
            L.append(L0.pop(d))
            L.append(L0.pop(d))
            if d != 0:
                d -= 1
        return L
    else:
        while len(L) != 10:
            L.append(L0.pop(d))
            if d != 0:
                d -= 1
            L.append(L0.pop(d))
        return L

def solve_1(n, target=5472):
    n = str(n)
    A = make_this_list()
    R = []
    i = 0
    b = -1
    while True:
        if b != -1:
            b = n.find(str(A[i]))
            if b == -1:
                return R
            R.append(n[b])
            return R
        b = n.find(str(A[i]))
        if b != -1:
            R.append(n[b])
        i += 1
        

#def compute_u(n_list,target=5472):
#    result = []
#    for i in range(len(n_list)):
#        a = (n_list[i] - target)
#        if a > 0:
#            a += 1
#        result.append(a)
#    return result

#def solve_2(n,target=5472):
#    """no degeneracy"""
#    n = str(n)
#    l = len(n)
#    N = [int(d) for d in n]
#    T = [int(d) for d in str(target)]
#    solution = ''
#    # 1st digit
#    M = range(l)
#    U = compute_u(N,T[-l])
#    U_abs = np.abs(np.array(U))
#    ex_index = min(M,key=U_abs.__getitem__)
#    if U[ex_index] < 0:
#        up = False
#    else:
#        up = True
#    # remaining digits
#    solution += str(N.pop(ex_index))
#    l -= 1
#    while l > 1:
#        M = range(l)
#        U = compute_u(N,T[-l])
#        U_abs = np.abs(np.array(U))
#        
#        if up:
#            ex_index = min(M,key=U_abs.__getitem__)            
#        else: 
#            ex_index = max(M,key=U_abs.__getitem__)
#        
#        solution += str(N.pop(ex_index))
#        l -= 1
#    solution += str(N[0])
#    return int(solution)
    

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


#def make_n1():
#    b = make_n()
#    if b == find_nearest(b): 
#        # more efficient: perform one random permutation
#        b = rd.choice(permutations(b)[1:])
#    return b

#def play():
#    b = make_n()
#    if b == find_nearest(b): 
#        b = rd.choice(permutations(b)[1:])
#    print('Rearrange the digits of %s to get the nearest number to %d!' % (b,500))
#    while True:
#        ans = input('->')
#        if ans == find_nearest(b):
#            print('perfect')
#            break
#        elif ans not in permutations(b):
#            print('Digits aren\'t matching. You must use the digits from \
#                  the number above.')
#    return None
#k = 0
##L = [910,956,249,847,123]
#while k < 5:
#    number = rd.randint(1000,9999)
##    number = L[k]
#    print('number: '+str(number))
#    print(int(solve(number)))
#    print(solve_2(number))
#    k += 1
#play()
#print(type(find_nearest('3876')))

# testing 16.09.19
#print(solve_3(2369))
#print(make_this_list())
