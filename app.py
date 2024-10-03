# name  >3 ur <= 50 character

name = input ("write your name:" )

# length 
if len(name) < 3 :
    print ("the length should be greater than 3")

elif len(name)>50 :
    print ("the length should be lessthan 50")

else :
    print ("excellent")



# nested if 

name = "chiraze"

if name != "ali":
    if name == "chiraze":
        print ("you are chiz")
    else:
        print ("not chiraze")
else: print ("you are Ali")


