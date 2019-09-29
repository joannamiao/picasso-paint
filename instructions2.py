from tkinter import *
from paintWindows import *


class instructions2(object):
    def __init__(self,window,c):
        self.window = window
        self.c = c
        self.backButton = Button(self.window, text = "Let's Draw!", command = self.back)
        self.backButton.place(relx= 0.9, rely = 0.9, height = 50, width = 90, anchor = CENTER)
        self.intro = Label(self.window, text = "Do you want to become the next Picasso? If so, this game is perfect for you!",font =("Helvetica",25),fg = "grey38")
        self.intro.place(x = 500, y = 120, anchor = CENTER)
        self.step1 = Label(self.window, text = "Rule 1: You and your team will pick a word first.\n Each will attempt to use all three layers to draw the word. \n Each person is assigned to one layer and must draw under 60 seconds. \n Think smart thought! You must draw everything in one line stroke for each brush!",font =("Helvetica",22),fg = "grey")
        self.step1.place(x = 500, y = 270, anchor = CENTER)
        self.step2 = Label(self.window, text = "Rule 2: After selecting a tool, you can use it only once.\n However, you may change the color of that tool if applicable. \n The spray paint brush is an exception as you can use it whenever and however \n many times you wish to, however you may not change the color.",font =("Helvetica",22),fg = "grey")
        self.step2.place(x = 500, y = 400, anchor = CENTER)
        self.backButtonOn = False
        self.activeButton = self.backButton
    
    def back(self):
        self.activateButton(self.backButton, backButton=True)
        windows(self.window,self.c)
        self.backButton.destroy()
        self.intro.destroy()
        self.step1.destroy()
        self.step2.destroy()
    
    #http://effbot.org/tkinterbook/button.htm
    def activateButton(self,someButton, backButton = False):
        self.activeButton.config(relief=RAISED)
        someButton.config(relief=SUNKEN)
        self.backButtonOn = backButton
