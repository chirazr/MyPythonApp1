from tkinter import *

top = Tk()
top.title("calculator")
top.minsize(300,300)


number1label = Label(text="First Number")
number1label.pack()


number1entry= Entry()
number1entry.pack()



number2label = Label(text="second Number")
number2label.pack()


number2entry= Entry()
number2entry.pack()



def addNum():
    num1= int(number1entry.get())
    num2 = int( number2entry.get())
    res = num1+num2
    resultLabel = Label(text="the result is "+ str(res))
    resultLabel.pack()




but = Button(text="Add", command=addNum)
but.pack()





top.mainloop()