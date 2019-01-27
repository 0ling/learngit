#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc(*numbers): # variable parameters
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
