"""Write a function exaggerate which exaggerates a string:

> exaggerate('i ate 3 potstickers') # ‘i ate 6 potstickers’
> exaggerate('the food is good here') # ‘the food is great here’

It should double all the numbers in the string, and it should replace "good" with "great," "bad" with "terrible," and anything else you can think of."""

"""s = "I ate 3 potstickers"
Current_first_word = s.split(" ")[0] #this one gets the first word of the sliced string 
remaining_word = s[len(Current_first_word)+1:]# we need to get the remaining word here

#if the current object is an interger then we should return integer *2
print(Current_first_word)
print(remaining_word)
def exaggerate(s):
    Current_first_word = s.split(" ")[0] #this one slices all the words,, but we need to only get the first part of the sliced string"""
    

# Write a function spell_number that spells out the digits of in integer:

"""def numtoword(i):

    d = {0:"zero",1:"one",2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

    if len(str(i))==0:
        return ""
    else:
        number_string = str(i)
        first_number = int(number_string[0])
        rest_number = int(number_string[1:])
        print(rest_number)

        if len(str(rest_number)) != 1:
            return d[first_number]+ " " + numtoword(rest_number)
print(numtoword(1971))"""



