import re
#match()= searched for pattern at the begining of string
#findall() = to find all occurance of pattern in string
#finditer() =  to get iteratir to get all matches for given pattern in string
#sub()
s1 = "Sunday, Monday, Tuesday, Monday, Sunday"
pat = "sunday"
replacement = "Friday"

result = re.sub(pat, replacement, s1)
print(result)
result = re.sub(pat, replacement, s1, count=1)
print(result)

#\b : is used to define word boundary

result= re.sub(pat, replacement, s1, flags=re.IGNORECASE)
print(result)

#compile=> re.compile(pat) => optimized the load time if we use pattern multiple times

