"""
\D	-- Matches word characters.
"""

"""
For Better Understanding, try to compare it,
with: \w, \S
"""

# Imoprting 're' Module
import re

string = 'I love Python!'

# Matching words Characters
# Depends on the count of '\w'

match = re.search(r'\D', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\D\D', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\D\D\D', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\D\D\D\D', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\D\D\D\D\D\D', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    

# and so on ...
