# 'a' => this mode appends the content to end of the file
# if file does not exist it will create a file
#if file open with append mode it is not deleting any content of file
#but in write mode if open file content is deleted.
fh = open('myfile.txt', 'a')
fh.write("\n'a' mode use to append data")

fh.close()

fh = open('myfile2.txt', 'w')
#fh.write("'w' mode use to write data")
fh.close()

#r= read the file content as string
fh = open('myfile.txt', 'r')
#print(fh.read()) # we can pass length of string which we want to read eg fh.read(10) will red 10 char from file\
print(fh.readline()) #reads first line
print(fh.readline()) #reads second line
#if we use readline even if we dont have any line it will return empty strings which will confirm we are at the end of line
test= fh.readlines() #this returns all lines as list

for line in test:
    print(line.rstrip('\n'))

#fh=open('myfile1.txt', 'x') #mode x is to create new file, if file already exist it will throw an  error

#mode : r,a,w,x,t(to open file in text mode), b(to open file in binary mode) 'rt' is default mode