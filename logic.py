"""
English beggars 
Trouver ce que chaque mendiant d'une file obtient de x personnes, si chaque mendiant se présente en cyclant l'ordre de la file
"""
# Ma solution bien moche
def beggars(values, n):
    if n == 0:
        return []
    if n == 1:
        return [(sum(values))]
    nMoney = [0] * n
    pos = 0
    # Cycler la file de beggars dans la file de valeurs 
    # et compter ce qu'ils ramassent
    for i in values:
        if pos < n - 1:
            nMoney[pos] += i
            pos += 1
        elif pos == n - 1:
            nMoney[pos] += i
            pos = 0
    return nMoney

# Solution avec un slice/step
def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]