k = 7
n = 17

cambiar_base = lambda x, k: x%k if x//k == 0 else str(x%k) + str(cambiar_base(x//k, k))

def chequear_mirror(x):
    if x[0:len(x)//2:1] == x[len(x):(len(x)-1)//2:-1]:
        return True
    return False

def chequear(x, k, Q, total):
    if chequear_mirror(str(cambiar_base(x, k))):
        Q += 1
        total += x
    return Q, total


def calcular(n, k):
    total = 0
    Q = 0
    for j in range (1, 10):
        x = j
        Q, total = chequear(x, k, Q, total)
        if Q == n: return total
    j = 0
    while True:
        for i in range(10**j,10**(j+1)):
            x = int(str(i)+str(i)[::-1])
            Q, total = chequear(x, k, Q, total)
            if Q == n: return total
        for i in range(10**j,10**(j+1)):
            for s in range(0,10):
                x = int(str(i)+str(s)+str(i)[::-1])
                Q, total = chequear(x, k, Q, total)
                if Q == n: return total
        j+=1
print(calcular(n, k))