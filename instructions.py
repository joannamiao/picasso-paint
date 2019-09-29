from tkinter import *
from paintWindows import *

class instructions(object):
    def __init__(self,window,c):
        self.window = window
        self.c = c
        self.backButton = Button(self.window, text = "Let's Draw!", command = self.back)
        self.backButton.place(relx= 0.9, rely = 0.9, height = 50, width = 90, anchor = CENTER)
        self.intro = Label(self.window, text = "Do you want to become the next Picasso and master the art of one line art? \n If so, this game is perfect for you!",font =("Helvetica",25),fg = "grey38")
        self.intro.place(x = 600, y = 75, anchor = CENTER)
        self.step1 = Label(self.window, text = "Step 1: You and your team will pick a word first.\n Each person will attempt to use all three layers to draw the word. \n Each person is assigned to one layer and must draw under 45 seconds. \n Think smart though! You must draw everything in one lined strokes! \n If not then the game will automatically connect seperated lines, so be careful!",font =("Helvetica",22),fg = "grey")
        self.step1.place(x = 600, y = 200, anchor = CENTER)
        self.step2 = Label(self.window, text = "Step 2: After selecting the tool, you can draw the stroke.\n After each stroke, you must click the Layer button then the Save Layer button before moving on. \n You may change the color and brush size of that tool. \n Once finished customizing your tool's features, click on that tool button \n and see the circle icon below the slider update to the tool's current state. \n The spray paint brush is an exception as you can use it whenever and however \n many times you wish to, but you can't change its color or size.",font =("Helvetica",22),fg = "grey")
        self.step2.place(x = 600, y = 400, anchor = CENTER)
        self.step3 = Label(self.window, text = "Step 3: Once done with all the images, you can see everyone's finished images \n in a gallery-like animation by clicking on the Progress button, \n and click the Pause button to stop. \n You can also see the final product by clicking the Put Them Together button, \n and for a bit of pizzazz click on the Enhance It button!",font =("Helvetica",22),fg = "grey")
        self.step3.place(x = 600, y = 600, anchor = CENTER)
        self.backButtonOn = False
        self.activeButton = self.backButton
    
    def back(self):
        self.activateButton(self.backButton, backButton=True)
        windows(self.window,self.c)
        self.backButton.destroy()
        self.intro.destroy()
        self.step1.destroy()
        self.step2.destroy()
        self.step3.destroy()
    
    #http://effbot.org/tkinterbook/button.htm
    def activateButton(self,someButton, backButton = False):
        self.activeButton.config(relief=RAISED)
        someButton.config(relief=SUNKEN)
        self.backButtonOn = backButton
