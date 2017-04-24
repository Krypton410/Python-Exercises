def isVowel(char):
    '''
    char: a single letter of any case
    returns: True if char is a vowel and False otherwise.
    '''
    if char in ('a','e','i','o','u','A','E','I','O','U'):
        return True
    else:
        return False

print isVowel('b')