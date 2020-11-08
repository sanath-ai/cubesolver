import cv2
import numpy as np
import imutils
from ppadb.client import Client
import time
import pandas as pd
from rubik_solver import utils

def detect_color(low,high,img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, low, high)
    color = cv2.bitwise_and(img, img, mask=mask)
    if np.all(color == 0):
        return False
    else:
        return True
  
def format_individual_color(t):
    color = [None]*len(t)
    color[0] = t[0]
    color[1] = t[1]
    color[2] = t[4]
    color[3] = t[2]
    color[4] = t[3]
    color[5] = t[6]
    color[6] = t[5]
    color[7] = t[7]
    color[8] = t[8]
    return color

def check(big):
    binary = False
    for i in big:
        if i.count(None) == len(i):
            binary = True
        else:
            binary = False
    if binary:
        return True
    else:
        return False
            
def right(count):
    if count <= 3:
        device.shell("input swipe 217 1780 477 1780 2500")
    
def down(count):
    if count == 4:
        device.shell("input swipe 1000 933 1000 1203 2500")
    if count == 5:
        device.shell("input swipe 1000 933 1000 1203 2500")
        device.shell("input swipe 1000 933 1000 1203 2500")

def mid_point(a , b , c ,d):
    x = (c + a)/2 
    y = (d + b)/2 
    return int(x) , int(y) 

def Print(x, y, n):
    li = []
    # map to store the pairs
    # and their frequencies
    m = dict()
 
    # Store the coordinates along
    # with their frequencies
    for i in range(n):
        m[(x[i], y[i])] = m.get((x[i],y[i]), 0) + 1
 
    e = sorted(m)
     
    for i in e:
        li.append((i[0], i[1]))
    return li

def get_color(x , y, df):
    d0 = df[df['X'] == x]
    d1 = d0[d0['Y'] == y]
    clr = d1['color'].to_string()
    return clr

low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])

low_red = np.array([0,0,240])
high_red = np.array([0,0,255])

low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])

low_yellow = np.array([20, 100, 100])
high_yellow = np.array([30, 255, 255])

low_white = np.array([0,0,0])
high_white = np.array([0,0,255])

low_orange = np.array([10, 100, 20])
high_orange = np.array([25, 255, 255])

white = [None]*9
yellow = [None]*9
red = [None]*9
orange = [None]*9
blue = [None]*9
green = [None]*9

whitet = [None]*9
yellowt = [None]*9
redt = [None]*9
oranget = [None]*9
bluet = [None]*9
greent = [None]*9

dic = {'pos': [], 'color':[] }


big_list = [white,yellow,red,orange,green,blue]

adb =  Client(host = "127.0.0.1" , port = 5037)
devices = adb.devices()
device = devices[0]

yellowc = cv2.imread(r"E:\Sanath\whatsapp_det-20200904T181330Z-001\whatsapp_det\rubik\yellow.jpg")
redc = cv2.imread(r"E:\Sanath\whatsapp_det-20200904T181330Z-001\whatsapp_det\rubik\red.jpg")
bluec = cv2.imread(r"E:\Sanath\whatsapp_det-20200904T181330Z-001\whatsapp_det\rubik\blue.jpg")
greenc = cv2.imread(r"E:\Sanath\whatsapp_det-20200904T181330Z-001\whatsapp_det\rubik\green.jpg")
whitec = cv2.imread(r"E:\Sanath\whatsapp_det-20200904T181330Z-001\whatsapp_det\rubik\white.jpg")
orangec = cv2.imread(r"E:\Sanath\whatsapp_det-20200904T181330Z-001\whatsapp_det\rubik\orange.jpg")
colors = [yellowc,redc,bluec,greenc,whitec,orangec]
count = 0
for color in colors:
    t = []
    coord_x = []
    coord_y = []
    coord = []
    img = color
    img = img[821:1638, 162:937]
    img = cv2.resize(img, (int(img.shape[1]/2) , int(img.shape[0]/2)))
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    cnts = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    for cou , c in enumerate(cnts):
        M = cv2.moments(c)
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            cv2.rectangle(img , (x,y) , (x+w,y+h), (0,0,255), 2)
            i = img[y:y+h, x:x+w]
            a,b = mid_point(x,y,x+w,y+h)
            coord_x.append(a)
            coord_y.append(b)
            coord.append((a,b))
            # print(a,b)
            # dic['{}'.format(cou + 1)].append((a,b))
            if detect_color(low_blue,high_blue,i):
                # print("blue")
                # clr = "b"
                t.append("b")
            elif detect_color(low_yellow,high_yellow,i):
                # print("yellow")
                # clr = "y"
                t.append("y")
            elif detect_color(low_green,high_green,i):
                # print("green")
                # clr = "g"
                t.append("g")
            elif detect_color(low_orange,high_orange,i):
                # print("orange")
                # clr = "o"
                t.append("o")
            elif detect_color(low_white,high_white,i):
                # print("white")
                # clr = "w"
                t.append("w")
            else:
                # print("red")
                # clr = "r"
                t.append("r")
            # dic['{}'.format(cou + 1)].append(clr)
    # cv2.imshow("ggwp", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    for c in cnts:
        if  len(t) == 9 :
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.04 * peri, True)
            if len(approx) == 4:
                (x, y, w, h) = cv2.boundingRect(approx)
                i = img[y:y+h, x:x+w]
                if np.array_equal(color,bluec) :
                    bluet = t
                    t = []
                    clr = pd.DataFrame(bluet , columns = ["color"])
                    # print(blue)
    
                elif np.array_equal(color,yellowc):
                    yellowt = t
                    clr = pd.DataFrame(yellowt , columns = ["color"])
                    t = []
                    # print(yellow)
                elif np.array_equal(color,greent):
                    greent = t
                    clr = pd.DataFrame(greent , columns = ["color"])
                    t = []
                    # print(green)
                elif np.array_equal(color,orangec):
                     oranget = t
                     clr = pd.DataFrame(oranget , columns = ["color"])
                     t = []
                     # print(orange)
                elif np.array_equal(color,whitec):
                    whitet = t
                    clr = pd.DataFrame(whitet , columns = ["color"])
                    t = []
                    # print(white)
                elif np.array_equal(color,redc):
                    redt = t
                    clr = pd.DataFrame(redt, columns = ["color"])
                    t = []
                    # print(red)            
                    
            X = pd.DataFrame(coord_x , columns = ["X"] , index = None)
            Y = pd.DataFrame(coord_y , columns = ["Y"] , index = None)
    
            se = [X,Y,clr]
    
            df = pd.concat(se, axis=1 )
            df.reset_index(drop=True)
    
    
            coord.sort(key = lambda x: x[0]**2 + x[1]**2 )
    
            coord = format_individual_color(coord)
    
            for i in coord:
                dic['pos'].append(i)
                string = get_color(i[0],i[1],df).split(" ")
                dic['color'].append(string[4])
            if np.array_equal(color,bluec):
                blue = dic['color']
                print("blue : ",blue)
            elif np.array_equal(color, redc):
                red = dic['color']
                print("red : ",red)
            elif np.array_equal(color , yellowc):
                yellow = dic['color']
                print("yellow : ",yellow)
            elif np.array_equal(color , greenc):
                green = dic['color']
                print("green : ",green)
            elif np.array_equal(color , whitec):
                white = dic['color']
                print("white : ",white)
            elif np.array_equal(color , orangec):
                orange = dic['color']
                print("orange : ",orange)
            dic['pow'] = []
            dic['color'] = []
                
    cv2.imshow("ggwp", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
cube = yellow + blue + red + green + orange + white
cube = ''.join(cube)
utils.solve(cube, 'Beginner')
