"""
TIY-fizzbuzz
7 kyu fizzbuzz
"""
# Ma solution
def tiy_fizz_buzz(string):
    result = ''
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for c in string:
        if (not c.isalpha() or 
        (c not in vowels and not c.isupper())
        ):
            result += c   
        elif c.lower() in vowels and c.isupper():
            result+= 'Iron Yard'
        elif c in vowels:
            result += 'Yard'
        else:
            result += 'Iron'
    return result

# Solutions upvote
def tiy_fizz_buzz(string):
    return ''.join(
        'Iron Yard' if c in 'AEIOU' else
        'Yard' if c in 'aeiou' else
        'Iron' if c.isupper() else c
        for c in string
    )

def tiy_fizz_buzz(s):
    return "".join(("Iron "*c.isupper() + "Yard"*(c.lower() in "aeiou")).strip() or c for c in s)