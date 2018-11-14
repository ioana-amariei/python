# Write a function that calculates how many vowels are in a string.


def number_of_vowels(characters):
    count = 0
    for char in characters:
        if is_vowel(char):
            count += 1
    return count


def is_vowel(character):
    return character in 'aeiouAEIOU'


print("number of vowels: ", number_of_vowels("uafhcifqknGUYS"))
print("number of vowels: ", number_of_vowels("vbrfnl"))
print("number of vowels: ", number_of_vowels("aaaaaaa"))
