# Write a function that calculates how many vowels are in a string.


def number_of_vowels(characters):
    vowels = [c for c in characters if c in 'aeiouAEIOU']
    return len(vowels)


print("number of vowels: ", number_of_vowels("uafhcifqknGUYS"))
print("number of vowels: ", number_of_vowels("vbrfnl"))
print("number of vowels: ", number_of_vowels("aaaaaaa"))
