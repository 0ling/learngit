#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def person(name, age, *args, city = 'Beijing', job): # keyword-only argument
    print(name, age, city, job)
