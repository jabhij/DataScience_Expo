"""
\w	-- Matches word characters.
"""

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
