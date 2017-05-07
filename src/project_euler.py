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

def problem5(to):
    """
    https://projecteuler.net/problem=5
    
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    
    >>> problem5(10)
    2520
    
    >>> problem5(20)
    232792560
    
    """
    from sympy import factorint
    factor = {}
    for x in range(1, to+1):
        for base, exp in factorint(x).items():
            factor[base] = max(exp, factor.get(base, 0))
    else:
        result = 1
        for base, exp in factor.items():
            result *= base ** exp
        return result

def problem10(stop):
    """
    https://projecteuler.net/problem=10
    
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    
    >>> problem10(10)
    17
    
    >>> problem10(2000000)
    142913828922
    
    """
    from sympy import isprime
    return sum(
        x for x in range(2, stop) if isprime(x)
    )

def problem20(n):
    """
    https://projecteuler.net/problem=20
    
    n! means n × (n − 1) × ... × 3 × 2 × 1
    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    Find the sum of the digits in the number 100!

    >>> problem20(10)
    27

    >>> problem20(100)
    648

    """
    from sympy import factorial
    return sum(
        int(char) for char in str(factorial(n))
    )

