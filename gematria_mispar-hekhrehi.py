#!/usr/bin/env python3
# -*- coding: utf-8 -*-
gcode = {   'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8,
            'i':9,
            'j':600,
            'k':10,
            'l':20,
            'm':30,
            'n':40,
            'o':50,
            'p':60,
            'q':70,
            'r':80,
            's':90,
            't':100,
            'u':200,
            'v':700,
            'w':900,
            'x':300,
            'y':400,
            'z':500  }

word = input("Type the word: ").lower()
word = word.replace("ä", "a")
word = word.replace("ö", "o")
word = word.replace("ü", "u")
word = word.replace("ß", "s")

c=[]
for w in word:
    for e in gcode:
        if w==e:
            print(e, gcode[e])
            c.append(gcode[e])

print( sum(c) )
