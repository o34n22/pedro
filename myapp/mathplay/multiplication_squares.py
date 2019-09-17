#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:15:20 2019

@author: mig
"""

import random as rd
from sympy import isprime

def make(size):
    left, right = 1, 25
    primes = [i for i in range(left,right) if isprime(i)]
    L = []
    for i in range(size):
        L.append(rd.choice(primes))
    
    return L


class Multi:
    def __init__(self, size):
        self.size = size
        self.input = make(self.size)
    
    def give(self):
        H1 = self.input[0]*self.input[1]
        H2 = self.input[2]*self.input[3]
        V1 = self.input[0]*self.input[2]
        V2 = self.input[1]*self.input[3]
        return [H1,H2,V1,V2]

