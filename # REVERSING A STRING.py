# REVERSING A STRING

def reverse_string(my_string):
    reversed_string = my_string[::-1]
    return reversed_string


# COUNTING VOWELS

def count_vowels(text):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]

    for character in text:
        if character in vowels:
            count += 1
    return count


# UPPERCASE

def to_uppercase(lower_case_string):
    upper_case_string = lower_case_string.upper()
    return upper_case_string
    

# PALINDROME
def is_palindrome(text):
    normal_string = text.replace(" ", "").lower()
    palindrome_string = normal_string[::-1]
    if normal_string == palindrome_string:
        return True
    else:
        return False


# REPLACING SUB-STRING

def replace_substring(normal_string, word, replaced_word):
   replaced_string = normal_string.replace(word, replaced_word)
   return replaced_string
  

# SPLITTING STRING

def split_string(unsplitted_string, splitting_operator):
    splitted_string = unsplitted_string.split(splitting_operator)
    return splitted_string
    

# JOINING STRINGS
def join_strings(unjoined_strings, combine):
    joined_string = combine.join(unjoined_strings)
    return joined_string


# SUB-STRING

def find_substring(main_string, sub_string):
    sub_string = main_string.find(sub_string)
    return sub_string


# CAPITALIZING STRING

def capitalize_string(normal_string):
    capitalized_string  =  normal_string.capitalize()
    return capitalized_string