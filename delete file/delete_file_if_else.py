#Check if file exits, then delete it
import os
if os.path.exists("demo.txt"):
  os.remove("demo.txt")
else:
  print("The File Does Not Exist");
