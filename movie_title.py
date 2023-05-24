#!/usr/bin/python3
import re
n = """Title (2023)
Merlin (2008)
Prison Break (2012)
Vikings (2013)
Robbin Hood (2003)
White House Has Fallen (2004)
Black panther (2021)
"""

i = re.findall('^([A-Z].+)(\(\d{4}\))', n, re.MULTILINE)
lst = [i]
print(n)
