import re

s1= "Python is programming Language"

pat=r"old\new" #r is used to communicate to python that consider given input in raw format

pat=r"[A-Z][a-z][a-z]"

matchObj = re.search(pat,s1)
print(matchObj)

# \d : matches 1 digit character. It is similar to [0-9]
#\D :  matches anything except digit
#\s: matches any whitespace char also matches tab and \n
#\S: matches any character except \n, tab and white space
#\w : alphanumeric char a-z,0-9 and _
#\W : all but except alphanumeric char a-z,0-9 and _ like £@!$% etc
