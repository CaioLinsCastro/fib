# Calcula a sequência de Fibonacci (sqn)
n = int(input("n: "))
x, y = 1, 1

for _ in range(n):
    print(x)
    z = x
    x = y
    y = z + y
    
