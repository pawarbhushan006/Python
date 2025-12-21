import re

message = "The Current Python Version is 3.13, other version are 3.14, 3.12,3.11 "

match_object = re.search("[0-9][0-9]",message) #meta charecter passed in square bracket here any digit followed by any digit patter will be searched
print(match_object)

# wild card :
"""
.: means any character except new line \n character

"""

match_obj=re.search("[0-9].[0-9]","House 251/A")
print(match_obj)

mat_obj = re.search("[0-9][.][0-9]","House 251/A")
print(mat_obj)