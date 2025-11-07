#with statement simplifies resource management by automatically handling setup and cleanup task||
#with statement is close the file directly
with open("practice.txt",'wt') as fh:
    content=fh.read()
print(content)

#in case of an error with statement close the file and then throws the error