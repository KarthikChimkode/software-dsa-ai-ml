"""program to count the occurrences of each character in a given string. """
#lower is used to make sure that the program does't give Two Same Alpabhets which are in different cases
# If we remove lower for A it will give 1 and for a it will give 1 separetely 

def character_count(input_string):

    char_count = {}

    for char in input_string:
        if char.lower()  in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1

    for char, count in char_count.items():
        print(f"{char} : {count}")

    max_char = max(char_count, key = char_count.get) # to get which character repeated amximum times
    print(f"maximun times repeated {max_char}")

input_string = "KarthikChimkode"
character_count(input_string)