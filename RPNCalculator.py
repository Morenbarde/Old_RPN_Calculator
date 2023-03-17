#Nick Brown RPN Calculator Project

from tkinter import *


#Stack Classes
###############################################################################################
class StackNode:

    def __init__(self, myData, myNext):
        #Construct a new Stack Node
        self.data = myData
        self.next = myNext
        return
        

class Stack:

    def __init__(self):
        #Construct a new Stack. The first node and last node are the same. Size is 0        self.firstNode = LinkedListNode(None, None)
        self.firstNode = None 
        self.lastNode = self.firstNode
        self.size = 0
        return

    def Push(self, data):
        #Push a node onto the stack
        node = StackNode(data, None)

        if self.firstNode == None: 
            self.firstNode = node
            self.lastNode = node
        else:
            node.next = self.firstNode
            self.firstNode = node

        self.size += 1

        return

#-----------------------------------------
    def Pop(self):
        #Pop a node from the stack

        if self.size == 0:
            print ("Linked List is empty")
            frontData = None
        else:
            currentNode = self.firstNode
            frontData = currentNode.data

            # This is the case where we have only one node in the stack
            if currentNode.next == None:
                self.firstNode = None
                self.lastNode = self.firstNode
                self.size = self.size - 1
            else:

                # Here there is more than one node in the stack
                currentNode = currentNode.next
                self.firstNode = currentNode
                self.size = self.size - 1

        return frontData
    
#--------------------------------------
    def __str__(self):
        currentNode =  self.firstNode

        for i in range(self.size):
            print (currentNode.data)
            currentNode = currentNode.next

        return "Reached end of list.\n"

############################################################################


#Changes the entry box
def changeEntry(entryboxnum):
    global entry
    entry.grid_remove()
    entry = Label(entryBox, text = entryboxnum)
    entry.grid(row = 1, columnspan = 1)
    return

#Builds number shown in entry box
def inputNum(num):
    global entryboxnum
    counter = 0
    #Prevents adding too many points to the input number
    if num == ".":
        for i in range(len(entryboxnum)):
            if entryboxnum[i] == ".":
                counter += 1
    if counter == 0:
        entryboxnum += num
        changeEntry(entryboxnum)
    return

#Clears the entry box
def clearBox():
    global entryboxnum
    entryboxnum = ""
    changeEntry(entryboxnum)
    return

#Enters number into stack to be operated on
def enterNumber():
    global entryboxnum, calcStack 
    if entryboxnum != "":
        calcStack.Push(entryboxnum)
        entryboxnum = ""
        print(calcStack)
    return

#Clears all previous info
def clearAll():
    global calcStack
    clearBox()
    for i in range(calcStack.size):
        x = calcStack.Pop()
        print(x)
    print(calcStack)

#Command for Subtract Button
def subtract():
    global calcStack, entryboxnum
    #Allows for the subtract button to change number to negative and back
    #This only works on the first number though
    if calcStack.size == 0 and entryboxnum != "" and entryboxnum != ".":
        newnum = float(entryboxnum)
        entryboxnum = str(newnum-(2*newnum))
        changeEntry(entryboxnum)
    elif calcStack.size == 1 and entryboxnum != "." and entryboxnum == "":
        x = calcStack.Pop()
        newnum = float(x)
        entryboxnum = str(newnum-(2*newnum))
        changeEntry(entryboxnum)
    #Actual subtract function
    enterNumber()
    if calcStack.size != 1 and calcStack.size != 0:
        num2 = calcStack.Pop()
        num1 = calcStack.Pop()
        num3 = float(num1) - float(num2)
        calcStack.Push(str(num3))
        changeEntry(num3)
    return

#Command for Add Button
def add():
    global calcStack
    enterNumber()
    if calcStack.size != 1 and calcStack.size != 0:
        num2 = calcStack.Pop()
        num1 = calcStack.Pop()
        num3 = float(num1) + float(num2)
        calcStack.Push(str(num3))
        changeEntry(num3)
    return

#Command for Multiply Button
def multiply():
    global calcStack
    enterNumber()
    if calcStack.size != 1 and calcStack.size != 0:
        num2 = calcStack.Pop()
        num1 = calcStack.Pop()
        num3 = float(num1)*float(num2)
        calcStack.Push(str(num3))
        changeEntry(num3)
    return

#Command for Divide Button
def divide():
    global calcStack, entryboxnum
    #Prevents division by zero, displays "ERROR" message
    if entryboxnum == "0":
        clearAll()
        entryboxnum = "ERROR"
        changeEntry(entryboxnum)
        entryboxnum = ""
    else:
        enterNumber()
        if calcStack.size != 1 and calcStack.size != 0:
            num2 = calcStack.Pop()
            num1 = calcStack.Pop()
            num3 = float(num1)/float(num2)
            calcStack.Push(str(num3))
            changeEntry(num3)
    return

#Creating Tkinter window
window = Tk()
window.title("RPN Calculator")
window.geometry("275x350")

#Establishing the entry box
entryBox = Frame(window)
entryBox.grid(row = 1, column = 1)

entryboxnum = ""
spacerOne = Label(entryBox, text = "")
entry = Label(entryBox, text = entryboxnum)
spacerTwo = Label(entryBox, text = "")
spacerOne.grid(row = 0, columnspan = 1)
entry.grid(row = 1, columnspan = 1)
spacerTwo.grid(row = 2, columnspan = 1)

#Creating frame for operation buttons
buttonFrame = Frame(window)
buttonFrame.grid(row = 2, column = 1)

#Creating operation buttons ################################################
enterButton = Button(buttonFrame, text = "ENTER", command = enterNumber)
clearButton = Button(buttonFrame, text = "CLR", command = clearAll)
clearEntryButton = Button(buttonFrame, text = "CLX", command = clearBox)
subtractButton = Button(buttonFrame, text = "-", command = subtract)
addButton = Button(buttonFrame, text = "+", command = add)
multiplyButton = Button(buttonFrame, text = "x", command = multiply)
divideButton = Button(buttonFrame, text = "/", command = divide)
pointButton = Button(buttonFrame, text = ".",
                     command = lambda num = ".": inputNum(num))
changeEntry("")
entryboxnum = ""

enterButton.config(height = 2, width = 15)
clearButton.config(height = 2, width = 8)
clearEntryButton.config(height = 2, width = 8)
subtractButton.config(height = 3, width = 6)
addButton.config(height = 3, width = 6)
multiplyButton.config(height = 3, width = 6)
divideButton.config(height = 3, width = 6)
pointButton.config(height = 3, width = 6)

enterButton.grid(row = 0, columnspan = 2)
clearButton.grid(row = 0, column = 3)
clearEntryButton.grid(row = 0, column = 2)
subtractButton.grid(row = 1, column = 0)
addButton.grid(row = 2, column = 0)
multiplyButton.grid(row = 3, column = 0)
divideButton.grid(row = 4, column = 0)
pointButton.grid(row = 4, column = 2)

#########################################################################

#Creating number buttons
counter = 3
for i in range(10):
    number = 9-i
    if number == 0:
        counter = 1
    counter -= 1
    b = Button(buttonFrame, text = str(number),
               command = lambda num=number: inputNum(str(num)))
    b.config(height = 3, width = 6)
    b.grid(row = i//3 + 1, column = counter + 1)
    if counter == 0:
        counter = 3

#create stack for entered numbers for operands to use.
calcStack = Stack()

window.mainloop()
