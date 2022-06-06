from msilib.schema import File


#f = open ("lesson1.txt")
f = open ("lesson2.txt" , "x")
#f = open ('img.bmp', "r+b") #read and write in binary

print (f.readline())

#*****
#r = opens a file for reading (default)
#w = opens a file for writing . Creates a new File
#x = opens a file for exclusive creation
#a = opens a file for appending at the end
#t = opens a file in text mode (default)
#b = opens in binary mode (cant read or write text)
#+ = opens a file for updating (reading and writing)
#***
with open ("lesson2.txt", "w" , encoding= 'utf -8') as f:
    f.write ("This is a new file\n")
    f.write ("Today is a cold day\n" )
    f.write ("We are learning Python\n")


f = open("lesson1.txt")
#reading the file
print(f.read())
f.close()