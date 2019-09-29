from tkinter import *
from paintWindows import *
from instructions import *

class startPage(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("Picasso's Palette")
        self.c = Canvas(self.window, bg='white', width=1200, height=1200)
        #http://effbot.org/tkinterbook/label.htm
        self.title = Label(self.window, text = "Welcome to Picasso's Palette!",font =("Helvetica",50),fg = "grey")
        self.title.place(x=600,y=300,anchor = CENTER)
        self.startButton = Button(self.window, text = "Start", command = self.start)
        self.startButton.place(relx= 0.33, rely = 0.55, height = 70, width = 100, anchor = CENTER)
        self.instructionsButton = Button(self.window, text= "Instructions",command = self.instructions)
        self.instructionsButton.place(relx = 0.66, rely = 0.55, height = 70, width = 100, anchor = CENTER)
        self.initVar()
        #https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
        self.c.grid(row=4, columnspan=10)
        self.window.mainloop()
    
    def initVar(self):
        self.startButtonOn = False
        self.instructionsButtonOn = False
        self.activeButton = self.startButton

        
    def start(self):
        self.activateButton(self.startButton, startButton=True)
        windows(self.window, self.c)
        # to get rid of label/button: https://stackoverflow.com/questions/12364981/how-to-delete-tkinter-widgets-from-a-window/12365098
        self.title.destroy()
        self.startButton.destroy()
        self.instructionsButton.destroy()

        
    def instructions(self):
        self.activateButton(self.instructionsButton, instructionsButton=True)
        instructions(self.window, self.c)
        self.title.destroy()
        self.startButton.destroy()
        self.instructionsButton.destroy()
        
    #http://effbot.org/tkinterbook/button.htm
    def activateButton(self,someButton, startButton = False, instructionsButton = False):
        self.activeButton.config(relief=RAISED)
        someButton.config(relief=SUNKEN)
        self.startButtonOn = startButton 
        self.instructionsButtonOn = instructionsButton 


if __name__ == '__main__':
    startPage()