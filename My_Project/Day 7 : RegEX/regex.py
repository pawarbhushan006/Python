#regular expression
import re
message = "The Current Python Version is 3.14, other version are 3.13, 3.12,3.11 "

# if python is present in string
print("Python" in message)
print("13" in message)
#to get the index of substring start
print(message.find('3.13'))
print(message.find('Python'))

"""
re.search(regex_pattern, string) => returns match object when there is match found , else returns None
"""

match_obj= re.search('13',message)
print(match_obj)