# classes for the different brush heads/colors
from tkinter import *
from tkinter.colorchooser import *


#for the sub toolbar for brushes/colors
class BrushToolBar(object):
    brushGroupsList= []
    rainbowBrushGroupsList=[]
    pencilGroupsList = []
    eraserGroupsList = []
    sprayPaintGroupsList = []

    #defining features of the color/brush toolbox
    def __init__(self,window,c):
        self.window = window
        self.c = c

        # for button code: https://www.tutorialspoint.com/python/tk_button.htm
        self.brushButton = Button(self.window, text='brush', command=self.useBrush)
        self.brushButton.grid(row=2, column=0)
        self.rainbowBrushButton = Button(self.window, text = "rainbow brush", command = self.useRainbowBrush)
        self.rainbowBrushButton.grid(row=2,column = 1)
        self.pencilButton = Button(self.window, text='pencil', command=self.usePencil)
        self.pencilButton.grid(row=2, column=2)
        self.colorButton = Button(self.window, text='color', command=self.pickColor)
        self.colorButton.grid(row=2, column=3)
        self.eraserButton = Button(self.window, text='eraser', command=self.useEraser)
        self.eraserButton.grid(row=2, column=4)
        self.sprayButton = Button(self.window, text = 'spray paint', command = self.sprayPaint)
        self.sprayButton.grid(row = 2,column=5)
        #slider: http://effbot.org/tkinterbook/scale.htm
        self.slider2 = Scale(self.window, from_=1, to=9, orient = HORIZONTAL,label="pencil")
        self.slider2.set(1)
        self.slider2.grid(row=2,column=6)
        self.slider1 = Scale(self.window,from_=10, to=20, orient = HORIZONTAL,label = "brushes/eraser")
        self.slider1.set(10)
        self.slider1.grid(row = 2, column =7)
        self.initVar()
        
    
    def initVar(self):
        self.oldX = None
        self.oldY = None
        self.lineWidth = None
        self.color = 'black'
        self.rainbowColors = []
        self.brushButtonOn = False
        self.pencilButtonOn = False
        self.eraserOn = False
        self.rainbowBrushOn = False
        self.rainbowBrushSelected = False
        self.rainbowBrushIndex = 0
        self.sprayPaintOn = False
        #self.lineWidthOrig = 0
        self.brushList=[]
        self.rainbowBrushList=[]
        self.pencilList=[]
        self.sprayPaintList=[]
        self.eraserList=[]
        #https://www.cs.cmu.edu/~112/notes/notes-animations-demos.html
        #Image: https://pngimage.net/dirt-smudge-png-4/
        self.sprayPaintImg = PhotoImage(file="spraypaint.png")
        self.activeButton = self.brushButton
        # properly respond to mouse click every iteration: https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)
    
    def useBrush(self):
        self.activateButton(self.brushButton,brushButton=True)
        #http://effbot.org/tkinterbook/scale.htm
        self.lineWidth = self.slider1.get()
        self.c.create_oval(900,0,1100,50,fill="white",outline='')
        self.c.create_oval(1025,10,(self.lineWidth+1025+3),(self.lineWidth+ 10+3),fill = self.color,outline = '')
        self.lineWidthOrig = self.lineWidth
    
    def useRainbowBrush(self):
        #http://effbot.org/tkinterbook/scale.htm
        self.lineWidth = self.slider1.get()
        if(self.rainbowBrushSelected==False):
            for i in range(5):
                tempcolor = askcolor(color=self.color)[1]
                self.rainbowColors.append(tempcolor)
            self.rainbowBrushSelected = True
        self.activateButton(self.rainbowBrushButton,rainbowBrush=True)
        firstcolor = self.rainbowColors[0]
        self.lineWidth = self.slider1.get()
        self.c.create_oval(900,0,1100,50,fill="white",outline='')
        self.c.create_oval(1025,10,(self.lineWidth+1025+3),(self.lineWidth+ 10+3),fill = firstcolor,outline = '')
        self.lineWidthOrig = self.lineWidth
        
    def usePencil(self):
        self.lineWidth = self.slider2.get()
        self.activateButton(self.pencilButton,pencilButton=True)
        self.c.create_oval(750,0,975,50,fill="white",outline='')
        self.c.create_oval(875,10,(self.lineWidth+875+4),(self.lineWidth+14),fill = self.color,outline = '')
        self.lineWidthOrig = self.lineWidth
        
    def pickColor(self):
        self.eraserOn = False
        self.rainbowBrushOn=False
        #https://knowpapa.com/cchoser/ 
        self.color = askcolor(color=self.color)[1]
        
    def useEraser(self):
        #http://effbot.org/tkinterbook/scale.htm
        self.lineWidth = self.slider1.get()
        self.activateButton(self.eraserButton,eraser = True)
        self.c.create_oval(900,0,1100,50,fill="white",outline='')
        self.c.create_oval(1025,10,(self.lineWidth+1025+3),(self.lineWidth+ 10+3))
        self.lineWidthOrig = self.lineWidth
    
    def sprayPaint(self):
        self.sprayPaint = True
        self.activateButton(self.sprayButton, sprayPaint = True)
    
    #http://effbot.org/tkinterbook/button.htm
    def activateButton(self,someButton, brushButton = False, pencilButton = False, eraser = False, rainbowBrush=False, sprayPaint = False):
        self.activeButton.config(relief=RAISED)
        someButton.config(relief=SUNKEN)
        self.activeButton = someButton
        self.brushButtonOn = brushButton
        self.pencilButtonOn = pencilButton
        self.eraserOn = eraser
        self.rainbowBrushOn= rainbowBrush
        self.sprayPaintOn = sprayPaint
    
    def paint(self,event):
        if self.sprayPaintOn==True:
            #https://www.cs.cmu.edu/~112/notes/notes-animations-demos.html
            self.c.create_image(event.x, event.y,anchor=S, image = self.sprayPaintImg)
            #here append the coordinates for each spray mark to 
            self.sprayPaintList.append([event.x,event.y])
            if(len(self.sprayPaintList)>0):
                BrushToolBar.sprayPaintGroupsList.append(self.sprayPaintList)
                #print(self.sprayPaintGroupsList)
                self.sprayPaintList=[]
            return 
        if self.eraserOn==True:
            fillColor = 'white'
            #to keep track of eraser marks when resizing
        elif self.rainbowBrushOn ==True:
            fillColor = self.rainbowColors[self.rainbowBrushIndex%5]
            self.rainbowBrushIndex+=1
        else:
            fillColor = self.color
        if(self.oldX and self.oldY):
            #create line smoothly, no lag: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_line.html
            self.c.create_line(self.oldX, self.oldY, event.x, event.y,width=self.lineWidth, fill = fillColor, capstyle = ROUND, smooth=TRUE,splinesteps=100)
            if(self.brushButtonOn==True):
                point = [self.oldX,self.oldY,fillColor,self.lineWidth]
                self.brushList.append(point)
            if(len(self.brushList)>0):
                #print(self.brushList)
                #print(BrushToolBar.brushGroupsList)
                BrushToolBar.brushGroupsList.append(self.brushList)
                self.brushList=[]
            if self.rainbowBrushOn==True:
                self.rainbowBrushList.append([self.oldX,self.oldY,fillColor,self.lineWidth])
            if(len(self.rainbowBrushList)>0):
                #print(self.rainbowBrushGroupsList)
                BrushToolBar.rainbowBrushGroupsList.append(self.rainbowBrushList)
                self.rainbowBrushList=[]
            if(self.pencilButtonOn==True):
                self.pencilList.append([self.oldX,self.oldY,fillColor,self.lineWidth])
            if(len(self.pencilList)>0):
                #print(self.pencilGroupsList)
                BrushToolBar.pencilGroupsList.append(self.pencilList)
                self.pencilList=[]
            if(self.eraserOn==True):
                self.eraserList.append([self.oldX,self.oldY,fillColor,self.lineWidth])
            if(len(self.eraserList)>0):
                #print(self.eraserGroupsList)
                BrushToolBar.eraserGroupsList.append(self.eraserList)
                self.eraserList=[]
        
        self.oldX = event.x
        self.oldY = event.y
    
                
        
    
    #after setting new points as old points we want to reset original old points as None's    
    def reset(self,event):
        self.oldX = None
        self.oldY = None




    
        
        
        
    
        