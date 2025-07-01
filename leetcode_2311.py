s = "10"
k = 2

cambiar_base = lambda k, n: str(k % n) if k // n == 0 else str(k % n) + str(cambiar_base(k // n, n))

def ejercicio(s, k):
        if s == "": s = "0"
        k = cambiar_base(k, 2)[::-1]
        if len(s) > len(k):
            s0 = (s[:len(s)-len(k):]).replace('1', '')
            s1 = (s[len(s)-len(k)::])
            if s1 > k:
                s1 = s1[1::]
            return len(s0)+len(s1)
        elif int(s)<=int(k):
            return len(s)
        else:
            return len(s)-1

print(ejercicio(s, k))