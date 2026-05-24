def reverse_string_greater_5(s):
    words = s.split()
    result = []

    for word in words:
        if len(word) >= 5: # if the word is greater than or equal to 5 characters
            result.append(word[::-1]) # reverse the word using slicing
        else:
            result.append(word) # if the word is less than 5 characters, add it to the result
        
    return ' '.join(result) # join the words back into a string


''' Here we have a function that takes a string and returns a new string with the words reversed 
if they are greater than or equal 5 characters.'''

# Test the function
print(reverse_string_greater_5("Hello world, this is a test string"))


