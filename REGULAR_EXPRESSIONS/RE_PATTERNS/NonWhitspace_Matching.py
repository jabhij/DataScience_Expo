"""
\S	--  Matches nonwhitespace.
"""

"""
For Better Understanding, try to compare it
with: \w, \D
"""

# Importing 're' Module
import re

string = 'When, nothing goes Right --> Go Left <--'

match = re.search(r'\S\S\S\S', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

## or

match = re.search(r'\S\S\S\S\S', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
## or

match = re.search(r'\S\S\S\S\S\S', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
## or

match = re.search(r'\S\S\S\S\S\S\S\S', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
