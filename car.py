#functions

def function_name ():
    #statement
    return 


def welcome_user ():

  print ("hello")
  print ("Welcome user")

welcome_user()



# input parameter

def welcome_user (name):

  print ("hello")
  print (f"Welcome {name}")

welcome_user("chiraze")

# input parameters

def welcome_user (first_name, last_name):

  print ("hello")
  print (f"Welcome {first_name} {last_name} ")

welcome_user(first_name="chiraze" , last_name="chiz")


# return function

def add(num1, num2):
   
   result = num1+num2

   print (result)
add(3,5)


def add(num1, num2):
   
   result = num1+num2

   return result
print(add(3,5))
