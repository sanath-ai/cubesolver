import cv2
import numpy as np
from ppadb.client import Client
import matplotlib.pyplot as plt
import time
adb =  Client(host = "127.0.0.1" , port = 5037)
devices = adb.devices()
device = devices[0]

Front = (564, 1176, 777 ,1071)
Right = (897,1494,924,1120)  
Up = (918,1177,597,1356)
Left = (564,1136,606,1671)
Down = (558,1713,879,1512)
Back = (543,864,264,981)

FrontI = (Front[2],Front[3],Front[0],Front[1])
BackI = (Back[2],Back[3],Back[0],Back[1])
RightI = (Right[2],Right[3],Right[0],Right[1])
UpI = (Up[2],Up[3],Up[0],Up[1])
DownI = (Down[2],Down[3],Down[0],Down[1])
LeftI = (Left[2],Left[3],Left[0],Left[1])

# def draw_movement(img):
    
def get_colors():
    colors = []
    for i in range(6):
        x = input("Color is : ")
        result = device.screencap()
        with open(str(x)+".jpg", "wb") as fp:
            fp.write(result)
        print("Change Color or End\n")
#     # img = cv2.imread("screen" + str(i) +".jpg")
#     # colors.append(img)
def get_end_phase():
    result = device.screencap()
    with open("end_new.jpg", "wb") as fp:
        fp.write(result)

def swipe(di):
    device.shell("input swipe " + str(di[0]) + " " + str(di[1]) +" " + str(di[2]) + " " + str(di[3])+" 100")
    
def SOLVE(li):
    for i in li:
        if i =='F':
            swipe(Front)
        if i == 'L':
            swipe(Left)
        if i == 'R':
            swipe(Right)
        if i == 'U':
            swipe(Up)
        if i == 'D':
            swipe(Down)
        if i == 'B':
            swipe(Back)
        if i =="F'":
            swipe(FrontI)
        if i == "L'":
            swipe(LeftI)
        if i == "R'":
            swipe(RightI)
        if i == "U'":
            swipe(UpI)
        if i == "D'":
            swipe(DownI)
        if i == "B'":
            swipe(BackI)
        if i =='F2':
            swipe(Front)
            time.sleep(0.4)
            swipe(Front)
        if i == 'L2':
            swipe(Left)
            time.sleep(0.4)
            swipe(Left)
        if i == 'R2':
            swipe(Right)
            time.sleep(0.4)
            swipe(Right)
        if i == 'U2':
            swipe(Up)
            time.sleep(0.4)
            swipe(Up)
        if i == 'D2':
            swipe(Down)
            time.sleep(0.4)
            swipe(Down)
        if i == 'B2':
            swipe(Back)
            time.sleep(0.4)
            swipe(Back)
        print(i)
    time.sleep(0.4)            

if __name__ == '__main__':
#     # get_colors()
#     cor = [(102,984), (573,792), (993,1035), (498,1284)]
    
#     img_end = cv2.imread('end.jpg')
#     print("Set the rubiks cube in the following manner \n")
#     for i in cor:
#         cv2.circle(img_end, i, 10, (255,255,255),-1)
#     # img_end = img_end[821:1638, 162:937]
#     img_end = cv2.resize(img_end, (int(img_end.shape[1]/2) , int(img_end.shape[0]/2)))
#     cv2.imshow("Set Co-ordinates",img_end)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     b=False
#     while(b==False):
        
#         get_end_phase()
#         img_new = cv2.imread(r'end_new.jpg')
#         for i in cor:
#             cv2.circle(img_new, i, 10, (255,255,255),-1)
#         img_new = cv2.resize(img_new, (int(img_new.shape[1]/2) , int(img_new.shape[0]/2)))
#         cv2.imshow("Check Image", img_new)
#         cv2.waitKey(0)
#         inpt = input("Are the coordinates set?[yes/no] ")        
#         if inpt =="yes":
#             b = True
    
#     cv2.destroyAllWindows()
    
# result = device.screencap()
# with open("red.png", "wb") as fp:
#     fp.write(result)
    pass