try:
    number = int(input("write number : "))
    print (number)
except ValueError: print ("error")
except Exception as e : print(e)
