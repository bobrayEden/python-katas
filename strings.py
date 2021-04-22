"""
Disemvowel trolls
Filtrer les voyelles d'une string
"""
# Ma solution
def disemvowel(s):
    return s.translate(s.maketrans('','','aeiouAEIOU'))

"""
Where my anagram at ?
Trouver les anagrammes de mot dans une liste de mots
"""
# Ma solution
def anagrams(word, words):
    result = []
    ref = sum(ord(ch) for ch in word)
    for w in words:
        if sum(ord(ch) for ch in w) == ref:
            result.append(w)
    return result 


# Solution pythonesque
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

"""
Stop gninnipS my sdrow
Retourner la string originale en inversant l'ordre des lettres des mots en contenant 5 ou plus
"""
# Ma solution
def spin_words(sentence):
    words = sentence.split()
    for i, x in enumerate(words):
        if len(x) > 4:
            words[i] = "".join(reversed(list(x)))
    s = ' '
    return s.join(words)

# Solution upvote
# Avec une grosse list comprehension
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

"""
Pig it Latin
Retour : Prendre la première lettre de chaque mot et la passer à la fin, laisser la ponctuation telle quelle
"""
# Ma solution : Le list(text.split()) n'est pas nécessaire car split() renvoie une liste
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalpha() else x for x in list(text.split()))
