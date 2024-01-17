#1
def count_vowels(str):
    num_vowels = 0
    vowels = "aeiou"
    for e2 in range (len(str)):
        if str[e2] in vowels:
            num_vowels += 1
            return num_vowels
        
#2 
def reverse_string(str):
    result = ''
    for com in range (len(str) -1, -1, -1):
        result += str [com]
    return result

#3
def remove_vowels(str):
    result = ''
    vowels = "aeiou"
    for e2 in range (len(str)):
        if str[e2] in vowels:
            result += 1
            return result
