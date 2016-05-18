"""
Matches digits. Equivalent to [0-9]
"""

# Importing 're' Module
import re

string = 'Ping me @ 000 - 007'

# Matching
match = re.search(r'\d', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\d\d', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\d\d\d', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\d\d\d\d', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\d\d\d\d\d', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
