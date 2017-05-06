def problem1(stop):
    " solved by katayama"
    sum = 0
    for x in range(1, stop):
        if (x%3==0) or (x%5==0):
            sum += x
    return sum

def problem2(stop):
    """
    written by miyoshi^^
    date 2017/05/06
    """

    a, b = 1, 2
    numlist = [a,b]
    while True:
        numlist.append(a+b)
        a, b = b, a+b
        if numlist[-1] > stop:
            numlist.pop()
            break

    sum = 0
    for x in numlist:
        if x % 2 == 0:
            sum += x
    return(sum)

def problem3(num):
    "Solved by: Katsuro"
    from sympy import factorint
    return max(factorint(num).keys())
