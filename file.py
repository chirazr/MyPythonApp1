#files

#open (filename, accessmode)

f = open ("myfile.txt", "w")

f.write ("hello there! \n hi ... \n")



f.close()

f = open ("myfile.txt", "r")

content = f.read()
print(content) 


f.close()



#pattern
import re

pattern = "^[a-zA-Z]*$"
text = input("write your name:")

if re.match(pattern,text):
    print("matched")
else:
    print("not matched")

languages = ["a","b"]
text = "ggjbhojuoiyy"
for item in languages:
    if re.search(item,text):
        print("found")
    else:
        print("not found")