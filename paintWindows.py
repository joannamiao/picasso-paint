from tkinter import *
from brushheads import *
from layers import *



class windows(object):
    def __init__(self,window, c):
        #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
        self.window = window
        self.c = c
        # for button code: https://www.tutorialspoint.com/python/tk_button.htm
        self.layer1Button = Button(self.window, text = "Layer1", command = self.useLayer1,bg = "blue")
        self.layer1Button.grid(row=0,column = 0)
        self.layer2Button = Button(self.window, text = "Layer2", command = self.useLayer2)
        self.layer2Button.grid(row=0,column = 1)
        self.layer3Button = Button(self.window, text = "Layer3", command = self.useLayer3)
        self.layer3Button.grid(row=0,column = 2)
        self.animateButton = Button(self.window, text = "Progress", command = self.animate)
        self.animateButton.grid(row=0,column = 3)
        self.pauseButton = Button(self.window, text="Pause Progress",command = self.pause)
        self.pauseButton.grid(row=0,column=4)
        self.mergeButton = Button(self.window, text = "Put them together!", command = self.merge)
        self.mergeButton.grid(row = 0, column =5)
        self.enhanceButton = Button(self.window,text="Enhance it!", command = self.enhance)
        self.enhanceButton.grid(row = 0,column = 6)
        self.pauseEnhanceButton = Button(self.window, text = "Pause Enhance", command = self.pauseEnhance)
        self.pauseEnhanceButton.grid(row = 0, column = 7)
        self.initVar()
    
    def initVar(self):
        self.layer1ButtonOn = False
        self.layer2ButtonOn = False
        self.layer3ButtonOn = False
        self.animateButtonOn = False
        self.pauseButtonOn = False
        self.startAnimating = False
        self.mergeButtonOn = False
        self.enhanceButtonOn = False
        self.pauseEnhanceButtonOn = False
        self.timerDelay = 1000
        self.countLayer = 4
        self.activeButton = self.layer1Button
        #https://www.cs.cmu.edu/~112/notes/notes-animations-demos.html
        #Image: https://pngimage.net/dirt-smudge-png-4/
        self.sprayPaintImg = PhotoImage(file="spraypaint.png")
    


    def useLayer1(self):
        #clear anything on canvas first before drawing on layer 1
        if(self.layer2ButtonOn == True or self.layer3ButtonOn==True or self.mergeButtonOn == True):
            #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
            self.c.delete("all")
        self.activateButton(self.layer1Button, layer1Button = True)
        Layer1(self.window,self.c)
        if(len(BrushToolBar.brushGroupsList)>0):
            Layer1.MasterList1.append(BrushToolBar.brushGroupsList)
        if(len(BrushToolBar.rainbowBrushGroupsList)>0):
            Layer1.MasterList1.append(BrushToolBar.rainbowBrushGroupsList)
        if(len(BrushToolBar.pencilGroupsList)>0):
            Layer1.MasterList1.append(BrushToolBar.pencilGroupsList)
        if(len(BrushToolBar.sprayPaintGroupsList)>0):
            Layer1.MasterList1.append(BrushToolBar.sprayPaintGroupsList)
        if(len(BrushToolBar.eraserGroupsList)>0):
            Layer1.MasterList1.append(BrushToolBar.eraserGroupsList)
        #reset all brush lists
        BrushToolBar.brushGroupsList = []
        BrushToolBar.rainbowBrushGroupsList = []
        BrushToolBar.pencilGroupsList = []
        BrushToolBar.eraserGroupsList = []
        BrushToolBar.sprayPaintGroupsList = []
        if(self.layer1ButtonOn == True):
            if(len(Layer1.MasterList1)>0):
                self.reDrawLayer(Layer1.MasterList1)
                
        
    
    def useLayer2(self):
        if(self.layer1ButtonOn == True or self.layer3ButtonOn==True or self.mergeButtonOn == True):
            #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
            self.c.delete("all")
        self.activateButton(self.layer2Button,layer2Button=True)
        Layer2(self.window,self.c)
        if(len(BrushToolBar.eraserGroupsList)>0):
            Layer2.MasterList2.append(BrushToolBar.eraserGroupsList)
        if(len(BrushToolBar.brushGroupsList)>0):
            Layer2.MasterList2.append(BrushToolBar.brushGroupsList)
        if(len(BrushToolBar.rainbowBrushGroupsList)>0):
            Layer2.MasterList2.append(BrushToolBar.rainbowBrushGroupsList)
        if(len(BrushToolBar.pencilGroupsList)>0):
            Layer2.MasterList2.append(BrushToolBar.pencilGroupsList)
        if(len(BrushToolBar.sprayPaintGroupsList)>0):
            Layer2.MasterList2.append(BrushToolBar.sprayPaintGroupsList)
        #reset all brush lists
        BrushToolBar.brushGroupsList = []
        BrushToolBar.rainbowBrushGroupsList = []
        BrushToolBar.pencilGroupsList = []
        BrushToolBar.eraserGroupsList = []
        BrushToolBar.sprayPaintGroupsList = []
        if(self.layer2ButtonOn == True):
            if(len(Layer2.MasterList2)>0):
                self.reDrawLayer(Layer2.MasterList2)
        
    
    def useLayer3(self):
        if(self.layer1ButtonOn == True or self.layer2ButtonOn==True or self.mergeButtonOn == True):
            #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
            self.c.delete("all")
        self.activateButton(self.layer3Button, layer3Button = True)
        Layer3(self.window,self.c)
        if(len(BrushToolBar.eraserGroupsList)>0):
            Layer3.MasterList3.append(BrushToolBar.eraserGroupsList)
        if(len(BrushToolBar.brushGroupsList)>0):
            Layer3.MasterList3.append(BrushToolBar.brushGroupsList)
        if(len(BrushToolBar.rainbowBrushGroupsList)>0):
            Layer3.MasterList3.append(BrushToolBar.rainbowBrushGroupsList)
        if(len(BrushToolBar.pencilGroupsList)>0):
            Layer3.MasterList3.append(BrushToolBar.pencilGroupsList)
        if(len(BrushToolBar.sprayPaintGroupsList)>0):
            Layer3.MasterList3.append(BrushToolBar.sprayPaintGroupsList)
        #reset all brush lists
        BrushToolBar.brushGroupsList = []
        BrushToolBar.rainbowBrushGroupsList = []
        BrushToolBar.pencilGroupsList = []
        BrushToolBar.eraserGroupsList = []
        BrushToolBar.sprayPaintGroupsList = []
        if(self.layer3ButtonOn == True):
            if(len(Layer3.MasterList3)>0):
                self.reDrawLayer(Layer3.MasterList3)
     
    #redraws everything stored in master list
    def reDrawLayer(self,list):
        for brush in list:
            point = brush[0][0]
            if(len(point)==4):
                for i in range(len(brush)-1):
                    self.c.create_line(brush[i][0][0], brush[i][0][1], brush[i+1][0][0],brush[i+1][0][1],width=brush[i][0][3], fill = brush[i][0][2], capstyle = ROUND, smooth=TRUE,splinesteps=100)
            elif(len(point)==2):
            #this point is a spraypaint stroke
                for i in range(len(brush)):
                    self.c.create_image(brush[i][0][0], brush[i][0][1],anchor=S, image = self.sprayPaintImg)
  
    def animate(self):
        self.activateButton(self.animateButton, animateButton = True)
        self.startAnimating = True
        self.timerCalls = 0
        self.timerDelay = 1000
        self.startAnimation()
                
    
    def pause(self):
        self.activateButton(self.pauseButton, pauseButton=True)
        self.startAnimating = False
        self.startAnimation()
        self.c.delete("all")
        
    def startAnimation(self):
        if(self.startAnimating==True):
                self.c.delete("all")
                self.timerCalls +=1 
                if(self.timerCalls%3==1):
                    self.reDrawLayer(Layer1.MasterList1)
                elif(self.timerCalls%3==2):
                    self.reDrawLayer(Layer2.MasterList2)
                elif(self.timerCalls%3==0):
                    self.reDrawLayer(Layer3.MasterList3)
                #https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#timerFired
                self.c.after(self.timerDelay,self.startAnimation)

    def merge(self):
        self.c.delete("all")
        self.activateButton(self.mergeButton,mergeButton = True)
        self.reDrawLayer(Layer3.MasterList3)
        self.reDrawLayer(Layer2.MasterList2)
        self.reDrawLayer(Layer1.MasterList1)
    
    def enhance(self):
        self.activateButton(self.enhanceButton,enhanceButton = True)
        self.startEnhancing = True
        self.enhanceLayers()
    
    def pauseEnhance(self):
        self.activateButton(self.pauseEnhanceButton, pauseEnhance = True)
        self.startEnhancing = False
        self.enhanceLayers()
        self.c.delete("all")
    
        
    def enhanceLayers(self):
        if(self.startEnhancing == True):
            self.c.delete("all")
            #self.countLayer = 4
            list1 = Layer1.MasterList1
            list2 = Layer2.MasterList2
            list3 = Layer3.MasterList3
            self.reDrawLayer(list3)
            self.reDrawLayer(list2)
            self.reDrawLayer(list1)
            #since we only want 3 frames: 0, 1, and 2 frame
            if(self.countLayer >= 3):
                self.moveLayer1Foward(list1)
                self.moveLayer2Foward(list2)
                self.moveLayer3Foward(list3)
                self.c.after(self.timerDelay,self.enhanceLayers)
                self.countLayer -= 1
            elif(self.countLayer >= 1):
                self.moveLayer1Back(list1)
                self.moveLayer2Back(list2)
                self.moveLayer3Back(list3)
                self.c.after(self.timerDelay,self.enhanceLayers)
                self.countLayer -= 1
            elif(self.countLayer == 0):
                self.countLayer = 4
                self.c.after(self.timerDelay,self.enhanceLayers)
        
        
    def moveLayer1Foward(self,list):
        #layer 1 moves horizontally
        for brush in list:
            for point in brush:
                point[0][0] -= 60
    
    def moveLayer1Back(self,list):
        for brush in list:
            for point in brush: 
                point[0][0] += 60
    
    def moveLayer2Foward(self,list):
        #layer 2 moves vertically
        for brush in list:
            for point in brush:
                point[0][1] += 60
    
    def moveLayer2Back(self,list):
        for brush in list:
            for point in brush:
                point[0][1] -= 60
    
    def moveLayer3Foward(self,list):
        #layer 3 moves diagonally 
        for brush in list: 
            for point in brush:
                point[0][0] -= 60
                point[0][1] += 60
    
    def moveLayer3Back(self,list):
        for brush in list:
            for point in brush:
                point[0][0] += 60
                point[0][1] -= 60
    
        
    #http://effbot.org/tkinterbook/button.htm
    def activateButton(self,someButton, layer1Button = False,layer2Button=False,layer3Button=False,animateButton=False,pauseButton=False,mergeButton = False,enhanceButton = False,pauseEnhance = False):
        self.activeButton.config(relief=RAISED)
        self.activeButton = someButton
        self.layer1ButtonOn = layer1Button
        self.layer2ButtonOn=layer2Button
        self.layer3ButtonOn = layer3Button
        self.animateButtonOn=animateButton
        self.pauseButtonOn = pauseButton
        self.mergeButtonOn = mergeButton
        self.enhanceButtonOn = enhanceButton 
        self.pauseEnhanceButtonOn = pauseEnhance
        

   


