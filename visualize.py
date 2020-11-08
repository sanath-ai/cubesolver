import cv2
import numpy as np
import math 
def draw(x,y,img,color):
    w=h=30
    cv2.rectangle(img , (x,y), (x+w,y+h), color[0],-1)
    cv2.rectangle(img , (x+w,y), (x+2*w,y+h), color[1],-1)
    cv2.rectangle(img , (x+2*w,y), (x+3*w,y+h), color[2],-1)
    
    
def draw_phase(x,y,img,color):
    draw(x,y,img,[color[0],color[1],color[2]])
    draw(x,y+h,img,[color[3],color[4],color[5]])
    draw(x,y+2*h,img,[color[6],color[7],color[8]])
    
def str2color(li):
    for i,ele in enumerate(li):
        if ele == 'r':
            li[i] = Red
        if ele == 'b':
            li[i] = Blue
        if ele == 'y':
            li[i] = Yellow
        if ele == 'g':
            li[i] = Green
        if ele == 'w':
            li[i] = White
        if ele == 'o':
            li[i] = Orange
            
    return li

def draw_all_phase(color):
    padding = 5
    draw_phase(x,y,img,str2color(color[0]))
    draw_phase(x+3*w+padding,y,img,str2color(color[1]))
    draw_phase(x+6*w+2*padding,y,img,str2color(color[2]))
    draw_phase(x+9*w+3*padding,y,img,str2color(color[3]))
    draw_phase(x+3*w+padding,y-3*h-padding,img,str2color(color[4]))
    draw_phase(x+3*w+padding,y+3*h+padding,img,str2color(color[5]))
    return img

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
 
Blue	= (0,0,255)[::-1] 	
White	= (255,255,255)[::-1] 	
Yellow	= (255,255,0)[::-1] 	
Green	= (0,128,0)[::-1] 	
Orange  =(255,105,0)[::-1] 	
Red	    = (255,0,0)[::-1] 	



img = np.zeros((700,700,3), np.uint8)

padding = 5
w = h = 30
x = 28
y=300

if __name__ == '__main__':
    # yellow =  ['w', 'y', 'y', 'r', 'y', 'o', 'g', 'g', 'b']
    # red =  ['g', 'g', 'y', 'w', 'r', 'r', 'o', 'y', 'r']
    # blue =  ['o', 'g', 'o', 'y', 'b', 'o', 'r', 'b', 'w']
    # green =  ['r', 'w', 'b', 'b', 'g', 'o', 'y', 'w', 'b']
    # white =  ['y', 'r', 'w', 'b', 'w', 'o', 'b', 'w', 'g']
    # orange =  ['o', 'g', 'g', 'b', 'o', 'r', 'r', 'y', 'w']
    # color = [blue , red , green , orange, yellow , white]
    # draw_all_phase(color)

    # cv2.imwrite("Black.jpg",img)
    # cv2.imshow("draw",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    pass