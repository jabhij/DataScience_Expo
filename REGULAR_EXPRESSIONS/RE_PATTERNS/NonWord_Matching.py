"""
\W	--  Matches nonword characters.
""""

# Importing 're ' module
import re

# Closely analyse this string
string = 'My number: ## 000 - 007'

# Matching non-words 
match = re.search(r'\W\W\W', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
    
## or

# Closely analyse this string
string = 'My number : ## 000 - 007'

# Matching non-words 
match = re.search(r'\W\W\W', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    

## or

# Closely analyse this string
string = 'My number : ## 000 - 007'

# Matching non-words 
match = re.search(r'\W\W\W\W', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    

## or

# Closely analyse this string
string = 'My number : ## 000 - 007'

# Matching non-words 
match = re.search(r'\W\W\W\W\W', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
