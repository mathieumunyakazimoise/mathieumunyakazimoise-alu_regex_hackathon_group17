#!/usr/bin/python3
import re
n = """ISBN 123-2-456-67844-4
ISBN 123-2-456-67844-3
ISBN 123-2-456-67844-5
vqbnks ISBN 123-2-456-67844-6 zret
ISBN 123-2-456-67844-7 zert
"""

i = re.findall('ISBN \d{3}-\d-\d{3}-\d{5}-\d', n, re.MULTILINE)

print('\n'.join(i))
