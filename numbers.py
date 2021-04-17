"""
Power of 2 in range n
"""
# Solution
def powers_of_two(n):
    return [pow(2, x) for x in range(n + 1)]

"""
Parabolic Arc Length
Approximer une longueur d'arc en f(nb interval) d'une courbe avec x dans [0 - 1] et y = x * x
"""
# i.e. on calcule les coordonnées de segments puis leur longueur
# n : number of intervals
# Ma solution
from math import sqrt, fabs
def len_curve(n):
    # p : coordonnées des points pris sur la courbe
    p = []
    for i in range(0, n + 1):
        if i < n:
            x = i * 1/n
            y = x * x
            p.append([x, y])
        else:
            p.append([1, 1])
    # Calcul de la longueur des segments        
    length = 0
    for u in range(0, len(p) - 1):
        length += sqrt(pow(fabs(p[u][0] - p[u + 1][0]),2) + pow(fabs(p[u][1] - p[u + 1][1]),2))
    return round(length, 9)

# Solution upvote
from math import sqrt
def len_curve(n):
    return round(sum(sqrt((2*k+1)**2/n/n + 1) for k in range(n))/n, 9)

"""
Make Readable
Format seconds as int to string as hh:mm:ss
"""
# Ma solution
def make_readable(seconds):
    hours, mod = divmod(seconds, 3600)
    min, sec = divmod(mod, 60)
    times = [hours, min, sec]
    res = ''
    for num, x in enumerate(times, start = 1):
        if x < 10:
            res += '0' + str(x)
        else:
            res += str(x)
        if num < 3:
            res += ':'
    return res

# Solution upvote
def make_readable(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)