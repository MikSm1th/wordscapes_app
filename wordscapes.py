#!/usr/bin/env python

import itertools

with open("words.txt") as dict_file:
    valid_words = [''.join(line.strip().split()).lower() for line in dict_file if len(line) <= 12]

letters = input('What are your letters?:')
for word_length in range(3, len(letters) + 1):
    words = set()
    for possible_word_tuple in itertools.permutations(letters, word_length):
        possible_word_string = ''.join(possible_word_tuple)
        if possible_word_string in valid_words:
            words.add(possible_word_string)

    print("Matching {} letter words:".format(word_length))
    for word in words:
        print("\t {}".format(word))
