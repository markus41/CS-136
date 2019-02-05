# Reading: 3.3

# Problems:

# Implementation note: put library and consumer code in different modules to practice working with that structure


# Write a recursive function that takes a string s and two strings x and y that returns a string that has all instances of x replaced with y in s.
# Example: replace(‘foo’, ‘o’, ‘z’) => ‘fzz’


def replace_string(inval, old, new):
    if inval == '':
        return ''
    if inval[0] == old:
        return new + replace_string(inval[1:], old, new)
    return inval[0] + replace_string(inval[1:], old, new)


print(replace_string('foo', 'o', 'z'))


# Write a recursive function that takes an array of ints and returns an array of all the even ints in the input array
def return_evens(lists):
    fo





# Write a recursive function that takes a string and returns the input string with all runs of duplicate characters replaced with just one of the character.
# Example: 'ffoobbaaquuuuuuxax' => 'fobaquxax'




# The above, but instead of replacing 'aaaa' with 'a', include the number of repetitions in the original: 'a4'





# 3.2.1




# 3.2.4