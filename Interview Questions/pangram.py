'''A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.'''



def pangram(st):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(st.lower())

#other method

def pangram(st):
    return all(letter in st.lower() for letter in 'abcdefghijklmnopqrstuvwxyz')

#other method
import string
def pangram(st):
    return set(string.ascii_lowercase) <= set(st.lower())

#other method

def pangram(st):
    return all(chr(i) in st.lower() for i in range(ord('a'), ord('z') + 1))

#other method

def pangram(st):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet:
        if letter not in st.lower():
            return False
    return True


#test
print(pangram("The quick brown fox jumps over the lazy dog"))
print(pangram("Hello world"))







