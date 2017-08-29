#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

alphabet = list(string.ascii_uppercase)
valpha   = alphabet[::-1]

word = input("Type the word: ").upper()

for letter in word:
  print("atbash for", letter, "=" , valpha[alphabet.index(letter)])
