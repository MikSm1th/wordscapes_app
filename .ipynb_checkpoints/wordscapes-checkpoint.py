#!/usr/bin/env python

import streamlit as st
import itertools

def main():
    st.header("A simple wordscapes app")
    st.subheader("A demo on how to use Streamlit")
    

if __name__ == "__main__":
    main()

#def run_wordscapes():
with open("words.txt") as dict_file:
    valid_words = [''.join(line.strip().split()).lower() for line in dict_file if len(line) <= 12]

#letters = input('What are your letters?:')
letters = st.text_input(label='What are your letters?', value='')
str_length = st.text_input(label='How long is your word?', value='')
int_length = int(str_length)
word_length =  int_length + 1
#for word_length in range(3, len(letters) + 1):
words = set()
for possible_word_tuple in itertools.permutations(letters, word_length):
    possible_word_string = ''.join(possible_word_tuple)
    if possible_word_string in valid_words:
        words.add(possible_word_string)

st.write("Matching {} letter words:".format(word_length))
for word in words:
    st.write("\t {}".format(word))
