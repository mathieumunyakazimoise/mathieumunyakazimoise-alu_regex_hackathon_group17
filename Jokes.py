#!/usr/bin/python3
import re

n = """Why did the cat ate the mouse? Because she is hungry.
Yes.Why did the matress was breoken? Because he is too weighty.
"""

i = re.findall('Why\sdid\sthe\s[a-z ]+\?\sBecause[a-z ]+\.', n, re.MULTILINE)

print('\n'.join(i))
