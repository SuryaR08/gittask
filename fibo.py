#Modified iterative code
def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        c = a + b
        a = b
        b = c

print(fibo(5))

