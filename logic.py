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

"""
Building towers
Pour un nombre d'étage n, renvoyer une liste [' * ', '***'] (ici: n=2)
"""
def tower_builder(n_floors):
    return [str('*' * (2 * n + 1)).center(1 + (n_floors - 1) * 2,) for n in range(n_floors)]

"""
Choose best sum
Dans le set ls, choisir le subset de longueur k dont la somme <= à la limite t
"""
# Ma solution, à noter : la ligne y = ls[:] plus nécessaire, on peut travailler directement depuis ls
# Zappé de refactor cet aspect. Possible de refactor la boucle for dans le retour, aussi
from itertools import combinations 
def choose_best_sum(t, k, ls):
    y = ls[:]
    max = 0
    test = set(list(combinations(y, k)))
    for x in test:
        path = sum(x)
        if path >= max and path <= t:
            max = path
    return (None if max == 0 else max)

# Solutions upvote 1
import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None

# Solution upvote 2
from itertools import combinations
def choose_best_sum(t, k, ls):
    return max((sum(v) for v in combinations(ls,k) if sum(v)<=t), default=None)

"""
Rain Fall
"""
# Solution
import numpy as np
import re
def get_target(town, strng):
    lst = strng.splitlines()
    return (x for x in lst if x.startswith(town + ":"))

def get_rain(target):
    pattern = re.compile('[0-9]*\.[0-9]*')   
    rain = pattern.findall(target)
    rain = [float(x) for x in rain]
    return rain

def mean(town, strng):        
    target = get_target(town, strng)
    rain = get_rain(''.join(target))
    print(rain)
    return np.mean(rain) if rain else -1
    
def variance(town, strng):
    target = get_target(town, strng)
    rain = get_rain(''.join(target))
    print(rain)
    return np.var(rain) if rain else -1
