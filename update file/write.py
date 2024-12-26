#If file not exist, it create new file then write data on file.
#If file already exist, It overwrite the write file data.

f = open("demo.txt","w")
f.write("Hey, I am Rajat")
f.close()
