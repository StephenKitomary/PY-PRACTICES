# Define a function called letter_pairs that takes a string of letters as input,
# and outputs those letters as pairs separated by spaces.  For example:
# letter_pairs(‘george’) # ‘ge eo or rg ge'
def letter_pairs(s):
    # Base case
    if (len(s) < 3):
        return s[0] + s[1]
    # Recursize case
    else:
        return s[0] + s[1] + ' ' + letter_pairs(s[1:])

letter_pairs('george') # 'ge eo or rg ge'



# Write a function called initials that takes a string of words, and returns a
# string with the first letter of each word separated by spaces.  For example,
# initials(‘you cannot always get what you want’) # ‘y c a g w y w’
def initials(s):
    # Base cases
    if s == '': # If string is blank, return blank
        return ''
    elif ' ' not in s: # If string is a single word, return the first char
        return s[0]

    #Recursive case
    else:
        # Split s between spaces, and grab the first word
        first_word = s.split(' ')[0]
        # Cut s down by the length of the first word + 1 (for the space)
        remaining_string = s[len(first_word) + 1:]
        # Return the first letter of first_word + ' ' + recursive call
        return first_word[0] + ' ' + initials(remaining_string)

initials('you cannot always get what you want')


# Write a function called copies that takes an integer and string, and returns
# the string repeated integer times.  For example, copies(3, ‘hello’) # ‘hello
# hello hello’.
def copies(n, word):
    # Base case
    if n == 1:
        return word

    # Recursive case
    return word + ' ' + copies(n-1, word)

copies(3, 'hello')

# Write a function called remove that takes a word and a string of words, and
# returns the string of words with any instances of word removed.  For example,
# remove_word(‘cannot’, ‘you cannot always get what you want’) # ‘you always get
# what you want’
def remove(word, s):
    # Base case: if s is blank, return a blank
    if s == '':
        return ''

    # Recursive case
    else:
        # Split s between spaces, and grab the first word
        first_word = s.split(' ')[0]
        # Cut s down by the length of the first word + 1 (for the space)
        remaining_string = s[len(first_word) + 1:]

        # If the first word matches the word to remove, skip it and recurse
        if first_word == word:
            return remove(word, remaining_string)
        else:
            # Otherwise, keep the first word and recurse
            return first_word + ' ' + remove(word, remaining_string)

# Example usage:
remove('cannot', 'you cannot always get what you want')

# Write a function called describe_time that takes a time in seconds, and
# returns a description of the time in terms of centuries, years, weeks, days,
# hours, minutes, and seconds.  For example: describe_time(22222) # ‘6 hours 10
# minutes 22 seconds’ and  describe_time(4967189641) # ‘1 century 57 years 20
# weeks 6 days 8 hours 54 minutes 1 seconds.’
def describe_time(seconds):

    # Constants for calculations
    seconds_in_century = 3155760000 # 100 years
    seconds_in_year = 31557600 # 1 year = 365.25 days
    seconds_in_week = 604800
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60

    # Recursive cases
    if seconds >= seconds_in_century:
        count = seconds // seconds_in_century
        return f'{count} century' + ('s' if count > 1 else '') + ' ' + describe_time(seconds % seconds_in_century)
    elif seconds >= seconds_in_year:
        count = seconds // seconds_in_year
        return f'{count} year' + ('s' if count > 1 else '') + ' ' + describe_time(seconds % seconds_in_year)
    elif seconds >= seconds_in_week:
        count = seconds // seconds_in_week
        return f'{count} week' + ('s' if count > 1 else '') + ' ' + describe_time(seconds % seconds_in_week)
    elif seconds >= seconds_in_day:
        count = seconds // seconds_in_day
        return f'{count} day' + ('s' if count > 1 else '') + ' ' + describe_time(seconds % seconds_in_day)
    elif seconds >= seconds_in_hour:
        count = seconds // seconds_in_hour
        return f'{count} hour' + ('s' if count > 1 else '') + ' ' + describe_time(seconds % seconds_in_hour)
    elif seconds >= seconds_in_minute:
        count = seconds_in_minute
        return f'{count} minute' + ('s' if count > 1 else '') + ' ' + describe_time(seconds % seconds_in_minute)
    elif seconds >= 1:
        return f'{seconds} second' + ('s' if seconds > 1 else '')
    # Base case (no more seconds to process)
    else:
        return ''

# Example usage:
print(describe_time(22222))       # Output: '6 hours 10 minutes 22 seconds'
print(describe_time(4967189641))  # Output: '1 century 57 years 20 weeks 6 days 8 hours 54 minutes 1 second'