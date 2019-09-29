from tkinter import *
from brushheads import *
from layers import *

# for all of these editing functions, only the brush tool marks will change
class scaleUpImg(object):
    #keeps track of how many times you scale up or down
    
    def scale(list,count):
        for i in range(2):
            for brush in list: 
                for point in brush:
                    if(point[0][0] <= 600 and point[0][1]<=600):
                        x = 600 - abs((600 - point[0][0])*2)
                        y = 600 - abs((600 - point[0][1])*2)
                    elif(point[0][0] > 600 and point[0][1] <= 600):
                        x = 600 - abs((600 - point[0][0])*2)
                        y = 600 + abs((600- point[0][1])*2)
                    elif(point[0][0] > 600 and point[0][1]>600):
                        x = 600 + abs((600 - point[0][0])*2)
                        y = 600 + abs((600 - point[0][1])*2)
                    elif(point[0][0]<= 600 and point[0][1] >600):
                        x = 600 + abs((600 - point[0][0])*2)
                        y = 600 - abs((600 - point[0][1])*2)
                    point[0][0] = x
                    point[0][1] = y
            
        
class scaleDownImg(object):
    def scale(list,count):
        for i in range(2):
            for brush in list: 
                for point in brush:
                    if(point[0][0] <= 600 and point[0][1]<=600):
                        x = 600 - abs((600 - point[0][0])/2)
                        y = 600 - abs((600- point[0][1])/2)
                    elif(point[0][0] > 600 and point[0][1] <= 600):
                        x = 600 - abs((600- point[0][0])/2)
                        y = 600 + abs((600- point[0][1])/2)
                    elif(point[0][0] > 600 and point[0][1]>600):
                        x = 600 + abs((600 - point[0][0])/2)
                        y = 600 + abs((600 - point[0][1])/2)
                    elif(point[0][0]<= 600 and point[0][1] >600):
                        x = 600 + abs((600 - point[0][0])/2)
                        y = 600 - abs((600 - point[0][1])/2)
                    point[0][0] = x
                    point[0][1] = y
                    
                    
class rotateImg(object):
    
    def rotate(list,count):
        if(count ==1):
            for brush in list:
                for point in brush:
                    if(point[0][0] <= 600 and point[0][1] <= 600):
                        x = 600 + abs(600-point[0][1])
                        y = 600 - abs(600-point[0][0])
                    if(point[0][0] > 600 and point[0][1] <= 600):
                        x = 600 + abs(600-point[0][1])
                        y = 600 + abs(600-point[0][0])
                    if(point[0][0] > 600 and point[0][1] > 600):
                        x = 600 - abs(600-point[0][1])
                        y = 600 + abs(600-point[0][0])
                    if(point[0][0] <= 600 and point[0][1] > 600):
                        x = 600 - abs(600-point[0][1])
                        y = 600 - abs(600-point[0][0])
                    point[0][1] = y
                    point[0][0] = x

        elif(count==2):
            for brush in list:
                for point in brush:
                    if(point[0][0] <= 600 and point[0][1] <= 600):
                        x = 600 + abs(600-point[0][1])
                        y = 600 - abs(600-point[0][0])
                    if(point[0][0] > 600 and point[0][1] <= 600):
                        x = 600 + abs(600-point[0][1])
                        y = 600 + abs(600-point[0][0])
                    if(point[0][0] > 600 and point[0][1] > 600):
                        x = 600 - abs(600-point[0][1])
                        y = 600 + abs(600-point[0][0])
                    if(point[0][0] <= 600 and point[0][1] > 600):
                        x = 600 - abs(600-point[0][1])
                        y = 600 - abs(600-point[0][0])
                    point[0][1]=y
                    point[0][0]=x

        elif(count==3):
            for brush in list:
                for point in brush:
                    if(point[0][0] <= 600 and point[0][1] <= 600):
                        x = 600 + abs(600-point[0][1])
                        y = 600 - abs(600-point[0][0])
                    if(point[0][0] > 600 and point[0][1] <= 600):
                        x = 600 + abs(600-point[0][1])
                        y = 600 + abs(600-point[0][0])
                    if(point[0][0] > 600 and point[0][1] > 600):
                        x = 600 - abs(600-point[0][1])
                        y = 600 + abs(600-point[0][0])
                    if(point[0][0] <= 600 and point[0][1] > 600):
                        x = 600 - abs(600-point[0][1])
                        y = 600 - abs(600-point[0][0])
                    point[0][1]=y
                    point[0][0]=x

        elif(count==4):
            for brush in list:
                for point in brush:
                    if(point[0][0] <= 600 and point[0][1] <= 600):
                        x = 600 + abs(600-point[0][1])
                        y = 600 - abs(600-point[0][0])
                    if(point[0][0] > 600 and point[0][1] <= 600):
                        x = 600 + abs(600-point[0][1])
                        y = 600 + abs(600-point[0][0])
                    if(point[0][0] > 600 and point[0][1] > 600):
                        x = 600 - abs(600-point[0][1])
                        y = 600 + abs(600-point[0][0])
                    if(point[0][0] <= 600 and point[0][1] > 600):
                        x = 600 - abs(600-point[0][1])
                        y = 600 - abs(600-point[0][0])
                    point[0][1]=y
                    point[0][0]=x
