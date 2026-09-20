def generstor_fibonachi(num:int):
    a  = 1
    b = 0
    c = 0

    while c<=num:
        yield c
        c = a + b
        a = b
        b = c

n = generstor_fibonachi(5)
for i in n:
    print(i)