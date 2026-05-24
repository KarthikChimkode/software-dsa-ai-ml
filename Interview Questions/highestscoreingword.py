def high(x):
    words = x.split()
    max_score = 0
    best_word = ""

    for word in words: 
        score = 0 # initialize the score to 0 for each word to be used in the loop and we use in for inside loop because it will start from 0 again for each word
        for char in word:
            score += ord(char) - 96 # ord is a function that returns the unicode code point for a given character and we use 96 because a is 97 in unicode
        
        if score > max_score: # if the score is greater than the max score, then we update the max score and the best word
            max_score = score
            best_word = word
    
    return best_word


print(high("man i need zany a taxi up to ubud")) # zany and taxi has same score but zany is first in the list
print(high("what time are we climbing up the volcano"))
print(high("take me to semynak"))


'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''