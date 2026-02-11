def nettoyer(m):
    n = ""
    for i in m:
        b = ord(i)
        if (b > 96 and b < 123) or (b > 64 and b < 91):
            a = chr(b)
            n = n + a
    return n

print(nettoyer("test pour voir si sa marche"))
        
def majuscule(m):
    mn = nettoyer(m)
    n = ""
    for i in mn:
        c = ord(i)
        c = c - 32
        a = chr(c)
        n = n + a
    return n

print(majuscule("attrappez les tous"))

def chiffrement(message, clé):
    n = ""
    mn = nettoyer(message)
    if (clé >= 0 and clé < 26):
        for i in mn:
            b = ord(i)
            c = b + clé
            a = chr(c)
            n = n + a
        return n
    
print(chiffrement("Test pour voir si sa marche",5))


def dechiffrement(message, clé):
    return chiffrement(message, -clé)

print(dechiffrement("Uftuqpvswpjstjtbnbsdif", 1))

def cryptanalyseFrequence(message):
    freq = {}
    mn = nettoyer(message)
    for i in mn:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    maximum = max(freq, key=freq.get)
    cle = (ord(maximum) - ord('e')) % 26
    return cle

print(cryptanalyseFrequence("iaezuirxoaoauoueeaeaaauie"))


    

    

