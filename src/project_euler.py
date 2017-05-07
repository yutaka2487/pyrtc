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
