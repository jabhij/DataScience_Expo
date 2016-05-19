"""
re.I	--  Performs case-insensitive matching.
Idea- (It's better to use it. Cause nothing and saves everything.)
"""

"""
For Better Understanding, try to compare it with, any type of matching where the case matters. 
For Example: $, ^ etc.
"""

# Importing 're' Module
import re

# Using ^ 
string = 'Python is Fun!'

# Matching
match = re.search(r'^python', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
# USing the Modifier
match = re.search(r'^python', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'


# or
# Using $
string = 'I\'m into Python!'

# Matching
match = re.search(r'python!$', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
# USing the Modifier
match = re.search(r'python!$', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
