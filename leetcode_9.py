x = 12121

def ejercicio(x):
    x = str(x)
    return x[:len(x)//2:1] == x[len(x):len(x)-len(x)//2-1:-1]

print(ejercicio(x))