import re

with open("student_details.txt","rt") as fh:
    data =fh.read()
pattern = r"\b[a-zA-Z]+[\w_.-]+[@][a-z]+[.][a-z]+\b"

match_obj= re.finditer(pattern,data)

for match in match_obj:
    print(match)