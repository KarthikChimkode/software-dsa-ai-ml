# Have the function CamelCase(str) take the str parameter being passed and return it in proper camel case format where the first letter of each word is capitalized (excluding the first letter). The string will only contain letters and some combination of delimiter punctuation characters separating each word.
# For example: if str is "BOB loves-coding" then your program should return the string bobLovesCoding.
# Examples
# Input: "cats AND*Dogs-are Awesome"
# Output: catsAndDogsAreAwesome
# Input: "a b c d-e-f%g"
# Output: aBCDEFG 

def CamelCases(s):
    words = []
    current = ""

    for ch in s:
        if ch.isalpha():
            current += ch
        else:
            if current:
                words.append(current)
                current = ""

    # add last word
    if current:
        words.append(current)

    if not words:
        return ""
    
    result = words[0].lower()

    for word in words[1:]:
        result += word.capitalize()

    return result

print(CamelCases("BOB loves-coding"))
print(CamelCases("cats AND*Dogs-are Awesome"))
print(CamelCases("a b c d-e-f%g"))


import re 

def CamelCaseRe(s):
    words = re.split(r'[^a-zA-Z]+', s)

    words = [w for w in words if w]

    if not words:
        return ""

    result = words[0].lower()

    for word in words[1:]:
        result += word.capitalize()

    return result

print(CamelCaseRe("BOB loves-coding"))
print(CamelCaseRe("cats AND*Dogs-are Awesome"))
print(CamelCaseRe("a b c d-e-f%g"))
