#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string, re

alphabet = list(string.ascii_uppercase)
valpha   = alphabet[::-1]

word = input("Type the word: ").upper()
word = word.replace("Ä", "A")
word = word.replace("Ö", "O")
word = word.replace("Ü", "U")
word = word.replace("ß", "S")

for letter in word:
  try:
    print("atbash for", letter, "=" , valpha[alphabet.index(letter)])
  except:
    print("Error with input", letter)
