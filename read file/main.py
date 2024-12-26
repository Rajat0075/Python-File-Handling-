#Create New File and Writen Content on file
f = open("demo.txt","w") #create file
f.write("Hey, I AM RAJAT") #write data on file
f.close() #file system close

#Read Writen Content of File
f = open("demo.txt","r") #create file
print(f.read()) #read file data
