def repeatedString(s, n):

    number_of_letter_a = s.count('a')
    string_len = len(s)
    remainder = n % string_len
    repeated_string = n // string_len
    number_of_letter_a_in_substring = s[:remainder].count('a')

    return number_of_letter_a * repeated_string + number_of_letter_a_in_substring


print repeatedString('a', 1000000000000)
