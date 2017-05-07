def problem1(stop):
    " solved by katayama"
    sum = 0
    for x in range(1, stop):
        if (x%3==0) or (x%5==0):
            sum += x
    return sum

def problem2(stop):
    " solved by miyoshi "

    a, b = 1, 2
    sum = b
    while True:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b
        if a+b > stop: break        
    return(sum)

def problem3(num):
    "Solved by: Katsuro"
    from sympy import factorint
    return max(factorint(num).keys())

def problem4(digit):
    """
    https://projecteuler.net/problem=4

    A palindromic number reads the same both ways. 
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. 
    Find the largest palindrome made from the product of two 3-digit numbers.
    
    >>> problem4(2)
    9009
    
    >>> problem4(3)
    906609
    
    """
    start = 10**(digit-1)
    stop = 10**digit
    cand = []
    for x in range(start, stop):
        for y in range(start, stop):
            z = x * y
            s = str(z)
            if s==s[::-1]:
                cand.append(z)
    return max(cand)

