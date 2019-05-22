from test_framework import generic_test

import collections
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    char_frequency_for_letter = collections.Counter(letter_text)
    char_frequency_for_magazine = collections.Counter(magazine_text)
    for k, v in char_frequency_for_letter.items():
    	if char_frequency_for_magazine[k] < v:
    		return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
