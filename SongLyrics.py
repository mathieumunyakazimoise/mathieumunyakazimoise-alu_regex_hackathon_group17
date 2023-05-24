#!/usr/bin/python3
import re
n = """[Verse 2] some lyrics.\n
[Verse 3][Verse 4] some lyrics
[Verse 5] some lyrics
"""

i = re.findall('\[Verse\s\d\]\s[a-z].+', n, re.MULTILINE)

print('\n'.join(i))
