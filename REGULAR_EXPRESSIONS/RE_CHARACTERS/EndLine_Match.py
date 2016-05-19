"""
$	--  Matches end of line.
Caution- (Matches end of the 'Line' not the 'String')
"""

# Importing 're' Module
import re

# Take a close look at string
# It will cause you- 'Try Something Else!'
string = 'I\'m into Python!!'

# Matching
match = re.search(r'Python!$', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# This will cause you- 'Try Something Else!'
# Matching
match = re.search(r'$Python!', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Take a close look at string
# It will cause you- 'Try Something Else!'
string = 'I\'m Python Lover!'

# Matching
match = re.search(r'Python!$', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Take a close look at string
# It will cause you- 'Try Something Else!'
string = 'Python is Fun!'

# Matching
match = re.search(r'Python!$', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# A bit complex case
# Analyse closely for a better understanding

string1 = 'I\'m into Python!'
string2 = 'Python is Fun!'
string3 = 'I\'m Python Lover!'

# Matching 
match1 = re.search(r'Python!$', string1)
match2 = re.search(r'Python!$', string2)
match3 = re.search(r'Python!$', string3)
# Case1 - Python at the 'End'
if match1:
    print 'Match1:', match1.group()
# Case2 - Python at the 'Beginning' 
elif match2:
    print 'Match2:', match2.group()
# Case3 - Python at the 'Middle'
elif match3:
    print 'Match3:', match3.group()
else:
    print 'Try Something Else!'
