#!/usr/bin/env python3

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
    takes two integers n and m
    and return True if n is a permuation of m
    """
    n, m = str(n), str(m)
    for i in n:
        b = n.find(m[0])
        if b == -1:
            return False
        m = m[1:]
        n = n[:b] + n[(b+1):]
    return True

def pose(target=500):
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

def solve(n,target=5472):
    P = permutations(n)
    D = target*np.ones(len(P),dtype=int)
    j = 0
    j_min = 0
    for p in P:
        D[j] = abs(target - int(p))
        if D[j] < D[j_min]: j_min = j
        j+=1
    return P[j_min]


def compute_u(n_list,digit):
    result = []
    for i in range(len(n_list)):
        a = (n_list[i] - digit)
        if a > 0:
            a += 1
        result.append(a)
    return result

def solve_2(n,target=5472):
    """no degeneracy"""
    n = str(n)
    l = len(n)
    N = [int(d) for d in n]
    T = [int(d) for d in str(target)]
    solution = ''
    # 1st digit
    M = range(l)
    U = compute_u(N,T[-l])
    U_abs = np.abs(np.array(U))
    ex_index = min(M,key=U_abs.__getitem__)
    if U[ex_index] < 0:
        up = False
    else:
        up = True
    # remaining digits
    solution += str(N.pop(ex_index))
    l -= 1
    while l > 1:
        M = range(l)
        U = compute_u(N,T[-l])
        U_abs = np.abs(np.array(U))
        
        if up:
            ex_index = min(M,key=U_abs.__getitem__)            
        else: 
            ex_index = max(M,key=U_abs.__getitem__)
        
        solution += str(N.pop(ex_index))
        l -= 1
    solution += str(N[0])
    return int(solution)
    

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
k = 0
#L = [910,956,249,847,123]
while k < 5:
    number = rd.randint(1000,9999)
#    number = L[k]
    print('number: '+str(number))
    print(int(solve(number)))
    print(solve_2(number))
    k += 1
#play()
#print(type(find_nearest('3876')))
