def pig_it(test):
    words = test.split()
    result = []

    for word in words:
        if word.isalpha(): # check if the word is a letter
            result.append(word[1:] + word[0] + "ay")
        else:
            result.append(word)

    return " ".join(result)

print(pig_it("Hello World"))




"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""