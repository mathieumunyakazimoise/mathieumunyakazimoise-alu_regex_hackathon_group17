#!/usr/bin/python3
import re
n = """Show Name 11-Jan-2022 
Show Name 23-Feb-2023 Episode Title"""

i = re.findall('\d{2}-[JFMASOND]..-\d{4}', n, re.MULTILINE)

print('\n'.join(i))
