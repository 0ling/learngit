#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def identity(name, age, **kw): # keyword argument
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age,'other:', kw)
