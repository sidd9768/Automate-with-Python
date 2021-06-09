#! /usr/bin/env python3

import re

upper_lower = re.compile(r"[A-Z].*[a-z]")
digit_reg = re.compile(r"[0-9]")

def pass_checker(password):
    if len(password) > 8:
        if upper_lower.search(password):
            if digit_reg.search(password):
                print('right')
            else:
                print("Password should contain at least one digit")
        else:
            print("Password should containt upper and lower case.")
    else:
        print("Password should be at least 8 characters.")


pass_checker("sdJawwdasad")
print("Done!")
