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