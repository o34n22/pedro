#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# todos: 
# instructional text / message on what to do
# control panel
# 
# 
# 
import os
import random as rd
import numpy as np
from math import ceil

base_dir = os.path.dirname(__file__)

def pose(target):
    number_of_digits = len(str(target))
    low  = 10**(number_of_digits-1)
    high = 10**number_of_digits - 1
    return rd.randint(low,high)


def get_search_list(target):
    number_of_digits = len(str(target))
    target = int(target)
    filename = os.path.join(base_dir,'search_lists.csv')
    with open(filename) as f:
        L = np.loadtxt(f,dtype=int,delimiter=' ')
    power = number_of_digits - 1
    line_index = ceil(2*target*0.1**power)
    return L[line_index]


def tail(n_tail,below=True):
    N = [int(d) for d in n_tail]
    N.sort(reverse=below)
    s = ''
    for d in N:
        s += str(d)
    return s


def solve(n, target):
    """
    finds the permutation of n which is nearest to target
    """
    if int(n) == int(target):
        return n
    n = str(n)
    if len(n) == 2: # only two digits left -> direct comparison
        distance_1 = abs(int(n) - int(target))
        distance_2 = abs(int(n[1]+n[0]) - int(target))
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
            t = str(target)[1:]
            inner = inner0 + solve(new_n,target=t)
            return inner
        if int(outer0) != -1 and int(outer0) < A[0]:
            outer = outer0 + tail(n[:c]+n[(c+1):],below=True)
        else:
            outer = outer0 + tail(n[:c]+n[(c+1):],below=False)
        out_distance = abs(int(outer) - int(target))
        t = str(target)[1:]
        new_n = n[:b]+n[(b+1):]
        inner = inner0 + solve(new_n,target=t)
        in_distance = abs(int(inner) - int(target))
        if out_distance < in_distance:
            return outer
        elif out_distance > in_distance:
            return inner
        else: # fix same distance here
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
        distance_1 = abs(int(outer_1) - int(target))
        distance_2 = abs(int(outer_2) - int(target))
        if distance_1 < distance_2:
            return outer_1
        elif distance_1 > distance_2:
            return outer_2
        else: # to be fixed...
            return outer_2


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



class Task:
    def __init__(self,target):
        self.target         = target        
        self.number         = pose(target)
        self.solution       = solve(self.number,self.target)
        self.ans            = ''
        self.description    = 'By moving around the digits of %s, find the number \
            nearest to %s.' % (self.number,target)
        self.blabla         = 'blabla'

    def post_answer(self,some_answer):
        self.ans      = some_answer
        # todo: log posted answers
        
    def check_answer(self):
        correct = self.solution == self.ans
        return correct

    def wrong(self):
        """
        yields a number of feedback messages if ans is False
        """
        if is_permutation(self.number,self.ans):
            message = 'It seems there is a number yet nearer to %s.' % self.target
        else:
            message = 'Digits aren\'t matching. You must use the digits from \
                      the number given.'
    #    else:
    #        message = "I\'m speechless."
        return message


# --------------- testing ----------------
#a = Task(5001)

