word = "aaaa"

def contar(word):
        contar = 1
        i = 0
        while i < len(word)-1:
            j = i+1
            while word[i] == word[j]:
                j+=1
                contar+=1
                if j == len(word):
                    break
            i = j
        return contar

print(contar(word))