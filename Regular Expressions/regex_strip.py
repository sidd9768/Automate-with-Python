#! /usr/bin/env python3

import re

def reg_strip(sentence, strip_char = ""):
    print("Original Sentence: " + sentence)
    if strip_char == "":
        updated_sent = re.sub(r"^\s+|\s+$", "", sentence)
        print("Stripped sentence: " + updated_sent)
    else:
        strp = strip_char
        updated_sent = re.sub(r"[{}]".format(strip_char), "", sentence)
        print("Stripped sentence: " +  updated_sent)

reg_strip(",,,,,rrttgg.....banana....rrr", ",.grt")
