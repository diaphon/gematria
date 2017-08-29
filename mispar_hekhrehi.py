#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string,re

alphabet = list(string.ascii_uppercase)
alphanum = list(range(1,len(alphabet)))

word = input("Type the word: ").upper()
word = word.replace("Ä", "A")
word = word.replace("Ö", "O")
word = word.replace("Ü", "U")
word = word.replace("ß", "S")

for letter in word:
    print( alphanum[alphabet.index(letter)] , end=" " )
