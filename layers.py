from tkinter import *
from brushheads import *
from editingTools import *
#from instructions2 import *
import pickle
import random

class Layer1(object):
    MasterList1 = []
    rotateCount1 = 0
    scaleCount1 = 0
    word = ""
    wordOn = False
    def __init__(self,window,c):
        self.window = window
        self.c = c
        self.toolsButton = Button(self.window, text = "Tools",command=self.useTools )
        self.toolsButton.grid(row=1,column=0)
        self.scaleUpButton = Button(self.window, text = "Scale Up",command= self.scaleUp)
        self.scaleUpButton.grid(row=1,column=1)
        self.scaleDownButton = Button(self.window, text = "Scale Down",command= self.scaleDown)
        self.scaleDownButton.grid(row=1,column=2)
        self.rotateButton = Button(self.window, text = "Rotate",command= self.rotate)
        self.rotateButton.grid(row=1,column=3)
        self.saveButton = Button(self.window, text= "Save Layer 1", command = self.save)
        self.saveButton.grid(row=1,column=4)
        self.clearButton = Button(self.window, text = "Clear All", command = self.clear)
        self.clearButton.grid(row = 1, column = 5)
        self.timerButton = Button(self.window, text = "Start Time", command = self.countTime)
        self.timerButton.grid(row = 1,column = 6)
        self.wordListButton = Button(self.window, text = "Word", command = self.getList)
        self.wordListButton.grid(row = 0, column = 8)
        self.initVar()
        try: 
            self.c.create_text(600,90,text = Layer1.word, fill = "grey38", font = "Helvetica 22")
        except: 
            pass
        if(Layer1.wordOn == False and Layer2.wordOn == False and Layer3.wordOn == False):
            try:
                self.reDrawSavedImg()
            except: 
                pass
    
    def reDrawSavedImg(self):
        #https://docs.python.org/3/library/pickle.html
        with open('data.p','rb') as f:
            Layer1.MasterList1 = pickle.load(f)[1]
        self.reDrawLayer(Layer1.MasterList1)
    
    
    def initVar(self):
        self.toolsButtonOn = False
        self.scaleUpButtonOn = False
        self.scaleDownButtonOn = False
        self.rotateButtonOn = False
        self.saveButtonOn = False
        self.clearButtonOn = False
        self.timerButtonOn = False
        self.instructionsButtonOn = False
        self.timeCount1 = 45  
        self.timerDelay = 1000
        self.wordLst = ['park','Pittsburgh','animal shelter','beach','amusement park', 'California','New York','airport','movie theatre','library','DisneyLand','church','cats','dogs','birds','frogs','mouses','dinosaurs','unicorns']
        self.wordListOn = False
        self.activeButton = self.toolsButton
        self.sprayPaintImg = PhotoImage(file="spraypaint.png")
    
    def useTools(self):
        self.activateButton(self.toolsButton,toolsButton=True)
        BrushToolBar(self.window,self.c)
    
        
    def scaleUp(self):
        self.activateButton(self.scaleUpButton, scaleUpButton=True)
        Layer1.scaleCount1 += 1
        scaleUpImg.scale(Layer1.MasterList1, Layer1.scaleCount1)
        #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
        self.c.delete("all")
        self.reDrawLayer(Layer1.MasterList1)
    
    def scaleDown(self):
        self.activateButton(self.scaleDownButton, scaleDownButton=True)
        Layer1.scaleCount1 -=1
        scaleDownImg.scale(Layer1.MasterList1, Layer1.scaleCount1)
        #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
        self.c.delete("all")
        self.reDrawLayer(Layer1.MasterList1)
    
    def rotate(self):
        self.activateButton(self.rotateButton, rotateButton=True)
        if(Layer1.rotateCount1==4):
            Layer1.rotateCount1 = 1
        else:
            Layer1.rotateCount1 += 1
        rotateImg.rotate(Layer1.MasterList1,Layer1.rotateCount1)
        #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
        self.c.delete("all")
        self.reDrawLayer(Layer1.MasterList1)
        
    def reDrawLayer(self,lst):
        for brush in lst:
            point = brush[0][0]
            if(len(point)==4):
                for i in range(len(brush)-1):
                    self.c.create_line(brush[i][0][0], brush[i][0][1], brush[i+1][0][0],brush[i+1][0][1],width=brush[i][0][3], fill = brush[i][0][2], capstyle = ROUND, smooth=TRUE,splinesteps=100)
            elif(len(point)==2):
            #this point is a spraypaint stroke
                for i in range(len(brush)):
                    self.c.create_image(brush[i][0][0], brush[i][0][1],anchor=S, image = self.sprayPaintImg)
    
    def save(self):
        self.activateButton(self.saveButton, saveButton = True)
        data = { 1: Layer1.MasterList1}
        #https://docs.python.org/3/library/pickle.html
        with open('data.p','wb') as f:
            pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
            
    def clear(self):
        self.activateButton(self.clearButton,clearButton = True)
        if(len(Layer1.MasterList1)>0):
            self.c.delete("all")
            Layer1.MasterList1 = []
            self.save()
    
        
    def countTime(self):
        self.activateButton(self.timerButton, timerButton = True)
        if(self.timeCount1 > 0):
            self.reDrawLayer(Layer1.MasterList1)
            self.c.create_rectangle(550,30,650,70,fill="white",width = 0)
            self.c.create_text(600,50,text = self.timeCount1, fill = "gray38", font = "Helvetica 22")
            self.timeCount1 -= 1
            self.c.after(self.timerDelay,self.countTime)
        else:
            self.c.create_rectangle(550,30,650,70,fill="white",width = 0)
            self.c.create_text(600,50,text = "Time's Up!" , fill = "red", font = "Helvetica 22")
    
    def getList(self):
        self.activateButton(self.wordListButton,wordList = True)
        self.c.delete("all")
        Layer1.MasterList1 = []
        Layer2.MasterList2 = []
        Layer3.MasterList3 = []
        Layer1.wordOn = True
        Layer1.word = random.choice((self.wordLst))
        self.c.create_text(600,90,text = Layer1.word, fill = "grey38", font = "Helvetica 22")
    
    
            
    def activateButton(self,someButton, toolsButton = False, scaleUpButton = False, scaleDownButton = False, rotateButton = False,saveButton = False, clearButton = False, timerButton = False, wordList = False,instructionButton = False):
        self.activeButton.config(relief=RAISED)
        someButton.config(relief=SUNKEN)
        self.activeButton = someButton
        self.toolsButtonOn = toolsButton
        self.scaleUpButtonOn = scaleUpButton
        self.scaleDownButtonOn = scaleDownButton
        self.rotateButtonOn = rotateButton
        self.saveButtonOn = saveButton
        self.clearButtonOn = clearButton 
        self.timerButtonOn = timerButton
        self.wordListOn = wordList
        self.instructionsButtonOn = instructionButton

class Layer2(object):
    MasterList2 = []#continue replacing class attribute for all instances made here
    rotateCount2 = 0
    scaleCount2 = 0
    wordOn = False
    def __init__(self,window,c):
        self.window = window
        self.c= c
        self.toolsButton = Button(self.window, text = "Tools",command=self.useTools)
        self.toolsButton.grid(row=1,column=0)
        self.scaleUpButton = Button(self.window, text = "Scale Up",command= self.scaleUp)
        self.scaleUpButton.grid(row=1,column=1)
        self.scaleDownButton = Button(self.window, text = "Scale Down",command= self.scaleDown)
        self.scaleDownButton.grid(row=1,column=2)
        self.rotateButton = Button(self.window, text = "Rotate",command= self.rotate)
        self.rotateButton.grid(row=1,column=3)
        self.saveButton = Button(self.window, text= "Save Layer 2", command = self.save)
        self.saveButton.grid(row=1,column=4)
        self.clearButton = Button(self.window, text = "Clear All", command = self.clear)
        self.clearButton.grid(row = 1, column = 5)
        self.timerButton = Button(self.window, text = "Start Time", command = self.countTime)
        self.timerButton.grid(row = 1,column = 6)
        self.wordListButton = Button(self.window, text = "Word", command = self.getList)
        self.wordListButton.grid(row = 0, column = 8)
        self.initVar()
        try: 
            self.c.create_text(600,90,text = Layer1.word, fill = "grey38", font = "Helvetica 22")
        except: 
            pass
        if(Layer1.wordOn == False and Layer2.wordOn==False and Layer3.wordOn==False):
            try:
                self.reDrawSavedImg()
            except: 
                pass
        
    def reDrawSavedImg(self):
        #https://docs.python.org/3/library/pickle.html
        with open('data2.p','rb') as f:
            Layer2.MasterList2 = pickle.load(f)[1]
        self.reDrawLayer(Layer2.MasterList2)
        
    def initVar(self):
        self.toolsButtonOn = False
        self.scaleUpButtonOn = False
        self.scaleDownButtonOn = False
        self.rotateButtonOn = False
        self.saveButtonOn = False
        self.clearButtonOn = False
        self.timerButtonOn = False
        self.timeCount2 = 45
        self.timerDelay = 1000
        self.wordLst = ['park','Pittsburgh','animal shelter','beach','amusement park', 'California','New York','airport','movie theatre','library','DisneyLand','church','cats','dogs','birds','frogs','mouses','dinosaurs','unicorns']
        self.wordListOn = False
        self.activeButton = self.toolsButton
        self.sprayPaintImg = PhotoImage(file="spraypaint.png")
       
    
    def useTools(self):
        self.activateButton(self.toolsButton,toolsButton=True)
        BrushToolBar(self.window,self.c)
        self.brushGroupsList2 = BrushToolBar.brushGroupsList
        
    def scaleUp(self):
        self.activateButton(self.scaleUpButton, scaleUpButton=True)
        Layer2.scaleCount2 += 1
        scaleUpImg.scale(Layer2.MasterList2, Layer2.scaleCount2)
        #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
        self.c.delete("all")
        self.reDrawLayer(Layer2.MasterList2)
    
    def scaleDown(self):
        self.activateButton(self.scaleDownButton, scaleDownButton=True)
        Layer2.scaleCount2 -=1
        scaleDownImg.scale(Layer2.MasterList2, Layer2.scaleCount2)
        #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
        self.c.delete("all")
        self.reDrawLayer(Layer2.MasterList2)
    
    def rotate(self):
        self.activateButton(self.rotateButton, rotateButton=True)
        if(Layer2.rotateCount2==4):
            Layer2.rotateCount2 = 1
        else:
            Layer2.rotateCount2 += 1
        rotateImg.rotate(Layer2.MasterList2,Layer2.rotateCount2)
        self.c.delete("all")
        self.reDrawLayer(Layer2.MasterList2)

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
    
    def save(self):
        self.activateButton(self.saveButton, saveButton = True)
        data2 = { 1: Layer2.MasterList2}
        #https://docs.python.org/3/library/pickle.html
        with open('data2.p','wb') as f:
            pickle.dump(data2,f,pickle.HIGHEST_PROTOCOL)
            
    def clear(self):
        self.activateButton(self.clearButton,clearButton = True)
        if(len(Layer2.MasterList2)>0):
            self.c.delete("all")
            Layer2.MasterList2 = []
            self.save()
    
    def countTime(self):
        self.activateButton(self.timerButton, timerButton = True)
        if(self.timeCount2 > 0):
            self.reDrawLayer(Layer2.MasterList2)
            self.c.create_rectangle(550,30,650,70,fill="white",width = 0)
            self.c.create_text(600,50,text = self.timeCount2, fill = "gray38", font = "Helvetica 22")
            self.timeCount2 -= 1
            self.c.after(self.timerDelay,self.countTime)
        else:
            self.c.create_rectangle(550,30,650,70,fill="white",width = 0)
            self.c.create_text(600,50,text = "Time's Up!" , fill = "red", font = "Helvetica 22")
        
    def getList(self):
        self.activateButton(self.wordListButton,wordList = True)
        self.c.delete("all")
        Layer1.MasterList1 = []
        Layer2.MasterList2 = []
        Layer3.MasterList3 = []
        Layer2.wordOn = True
        Layer1.word = random.choice((self.wordLst))
        self.c.create_text(600,90,text = Layer1.word, fill = "grey38", font = "Helvetica 22")
        
    def activateButton(self,someButton, toolsButton = False, scaleUpButton = False, scaleDownButton = False, rotateButton = False,saveButton=False,clearButton=False,timerButton=False,wordList = False):
        self.activeButton.config(relief=RAISED)
        someButton.config(relief=SUNKEN)
        self.activeButton = someButton
        self.toolsButtonOn = toolsButton
        self.scaleUpButtonOn = scaleUpButton
        self.scaleDownButtonOn = scaleDownButton
        self.rotateButtonOn = rotateButton
        self.saveButtonOn = saveButton
        self.clearButtonOn = clearButton
        self.timerButtonOn = timerButton
        self.wordListOn = wordList
        
class Layer3(object):
    MasterList3 = []
    rotateCount3 = 0
    scaleCount3 = 0
    wordOn = False
    def __init__(self,window,c):
        self.window = window
        self.c=c
        self.toolsButton = Button(self.window, text = "Tools",command=self.useTools)
        self.toolsButton.grid(row=1,column=0)
        self.scaleUpButton = Button(self.window, text = "Scale Up",command= self.scaleUp)
        self.scaleUpButton.grid(row=1,column=1)
        self.scaleDownButton = Button(self.window, text = "Scale Down",command= self.scaleDown)
        self.scaleDownButton.grid(row=1,column=2)
        self.rotateButton = Button(self.window, text = "Rotate",command= self.rotate)
        self.rotateButton.grid(row=1,column=3)
        self.saveButton = Button(self.window, text= "Save Layer 3", command = self.save)
        self.saveButton.grid(row=1,column=4)
        self.clearButton = Button(self.window, text = "Clear All", command = self.clear)
        self.clearButton.grid(row = 1, column = 5)
        self.timerButton = Button(self.window, text = "Start Time", command = self.countTime)
        self.timerButton.grid(row = 1,column = 6)
        self.wordListButton = Button(self.window, text = "Word", command = self.getList)
        self.wordListButton.grid(row = 0, column = 8)
        self.initVar()
        try: 
            self.c.create_text(600,90,text = Layer1.word, fill = "grey38", font = "Helvetica 22")
        except: 
            pass
        if(Layer1.wordOn == False and Layer2.wordOn == False and Layer3.wordOn ==False):
            try:
                self.reDrawSavedImg()
            except: 
                pass
    
    def reDrawSavedImg(self):
        #https://docs.python.org/3/library/pickle.html
        with open('data3.p','rb') as f:
            Layer3.MasterList3 = pickle.load(f)[1]
        self.reDrawLayer(Layer3.MasterList3)
        
    def initVar(self):
        self.toolsButtonOn = False
        self.scaleUpButtonOn = False
        self.scaleDownButtonOn = False
        self.rotateButtonOn = False
        self.saveButtonOn = False
        self.clearButtonOn = False
        self.timerButtonOn = False
        self.timeCount3 = 45
        self.timerDelay = 1000
        self.wordLst = ['park','Pittsburgh','animal shelter','beach','amusement park', 'California','New York','airport','movie theatre','library','DisneyLand','church','cats','dogs','birds','frogs','mouses','dinosaurs','unicorns']
        self.wordListOn = False
        self.activeButton = self.toolsButton
        self.sprayPaintImg = PhotoImage(file="spraypaint.png")
    
    def useTools(self):
        self.activateButton(self.toolsButton,toolsButton=True)
        BrushToolBar(self.window,self.c)
        
        
    def scaleUp(self):
        self.activateButton(self.scaleUpButton, scaleUpButton=True)
        Layer3.scaleCount3 += 1
        scaleUpImg.scale(Layer3.MasterList3, Layer3.scaleCount3)
        self.c.delete("all")
        self.reDrawLayer(Layer3.MasterList3)
    
    def scaleDown(self):
        self.activateButton(self.scaleDownButton, scaleDownButton=True)
        Layer3.scaleCount3 -=1
        scaleDownImg.scale(Layer3.MasterList3, Layer3.scaleCount3)
        #https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
        self.c.delete("all")
        self.reDrawLayer(Layer3.MasterList3)
    
    def rotate(self):
        self.activateButton(self.rotateButton, rotateButton=True)
        if(Layer3.rotateCount3==4):
            Layer3.rotateCount3 = 1
        else:
            Layer3.rotateCount3 += 1
        rotateImg.rotate(Layer3.MasterList3,Layer3.rotateCount3)
        self.c.delete("all")
        self.reDrawLayer(Layer3.MasterList3)

        
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
    
    def save(self):
        self.activateButton(self.saveButton, saveButton = True)
        data3 = { 1: Layer3.MasterList3}
        #https://docs.python.org/3/library/pickle.html
        with open('data3.p','wb') as f:
            pickle.dump(data3,f,pickle.HIGHEST_PROTOCOL)
            
    def clear(self):
        self.activateButton(self.clearButton,clearButton = True)
        if(len(Layer3.MasterList3)>0):
            self.c.delete("all")
            Layer3.MasterList3 = []
            self.save()
    
    def countTime(self):
        self.activateButton(self.timerButton, timerButton = True)
        if(self.timeCount3 > 0):
            self.reDrawLayer(Layer3.MasterList3)
            self.c.create_rectangle(550,30,650,70,fill="white",width = 0)
            self.c.create_text(600,50,text = self.timeCount3, fill = "gray38", font = "Helvetica 22")
            self.timeCount3 -= 1
            self.c.after(self.timerDelay,self.countTime)
        else:
            self.c.create_rectangle(550,30,650,70,fill="white",width = 0)
            self.c.create_text(600,50,text = "Time's Up!" , fill = "red", font = "Helvetica 22")
    
    def getList(self):
        self.activateButton(self.wordListButton,wordList = True)
        self.c.delete("all")
        Layer1.MasterList1 = []
        Layer2.MasterList2 = []
        Layer3.MasterList3 = []
        Layer3.wordOn = True
        Layer1.word = random.choice((self.wordLst))
        self.c.create_text(600,90,text = Layer1.word, fill = "grey38", font = "Helvetica 22")
    
    def activateButton(self,someButton, toolsButton = False, scaleUpButton = False, scaleDownButton = False, rotateButton = False,saveButton = False, clearButton = False,timerButton=False,wordList = False):
        self.activeButton.config(relief=RAISED)
        someButton.config(relief=SUNKEN)
        self.activeButton = someButton
        self.toolsButtonOn = toolsButton
        self.scaleUpButtonOn = scaleUpButton
        self.scaleDownButtonOn = scaleDownButton
        self.rotateButtonOn = rotateButton
        self.saveButtonOn = saveButton
        self.clearButtonOn = clearButton
        self.timerButtonOn = timerButton
        self.wordListOn = wordList
        
