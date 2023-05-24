#!/usr/bin/python3
import re
n = """@moise10.\n
[Verse 3]@moise[Verse 4]@moise12
[Verse 5]@moise1013
"""

i = re.findall('@[a-z\d]+', n, re.MULTILINE)

print('\n'.join(i))