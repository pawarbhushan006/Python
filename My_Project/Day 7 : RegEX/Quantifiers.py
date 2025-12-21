import re
from idlelib.pathbrowser import PathBrowser

message = "The Current Python Version is 3.13, other version are 3.14, 3.12,3.11 "

pat = "[a-z]{4}" #similar to [a-z][a-z][a-z][a-z] to repeat the pattern
matchObj = re.search(pat,message)
print(matchObj)

pat = "[A-Z][a-z]{2,4}" #similar to [A-Z][A-Z][a-z][a-z][a-z][a-z] to repeat the pattern
matchObj = re.search(pat,message)
print(matchObj)

#+ => matches one or more repetition of previous pattern in below example it will check for lower case char
pat = r"[A-Z][a-z]+"
matchObj = re.search(pat,message)
print(matchObj)

# ? => exactly 0 or 1 match
# * => matche 0 or more matches for pattern
# $ => end of pattern
# ^ => start of pattern
# () => to group multiple patterns

