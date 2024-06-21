# Jessica Uriostegui
# June 19,2024
 

# Lesson 4: Assignments | Regex

import re

names = "Abraham Lincoln, Andrew P Garfield, peter pan, Connor Milliken, Jordan Alexander Williams, Madonna, programming is cool"

def validate_names(names):
    pattern = r"\b[A-Z][a-z]+\s(?:[A-Z][a-z]*\s)?[A-Z][a-z]+\b"
    valid_names = []
    invalid_names = []
    name_list = names.split(", ")
    for name in name_list:
        if re.match(pattern, name):
            valid_names.append(name)
        else:
            invalid_names.append(name)
    return valid_names, invalid_names
valid_names, invalid_names = validate_names(names)
print("Valid names:", valid_names)
print("Invalid names", invalid_names)

