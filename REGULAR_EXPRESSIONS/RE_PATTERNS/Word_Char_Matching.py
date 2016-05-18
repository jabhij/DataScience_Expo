"""
\w	-- Matches word characters.
"""

"""
For Better Understanding, try to compare it
with: \S, \D
"""

# Importing 're' Module
import re
string = 'I love Python!'

# Matching words Characters
# Depends on the count of '\w'

match = re.search(r'\w', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\w\w', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\w\w\w\w', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\w\w\w\w\w', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\w\w\w\w\w\w', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
