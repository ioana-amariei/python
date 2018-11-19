# Write a function that receives two strings as parameters and returns the number of occurrences
# of the first string in the second.


def number_of_occurrences(first, second):
    return second.count(first)


print("Number of occurrences of the 'abc' string in 'abcdddabcabc' string is: ",
      number_of_occurrences("abc", "abcdddabcabc"))
