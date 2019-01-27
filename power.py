def power(x, n = 2): # positionary argument & default argument
    s = 1
    while n >= 0:
        n = n - 1
        s = s * x
    return s
