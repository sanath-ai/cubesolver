import cv2
import numpy as np
from ppadb.client import Client
import matplotlib.pyplot as plt
adb =  Client(host = "127.0.0.1" , port = 5037)
devices = adb.devices()
device = devices[0]

    
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

if __name__ == '__main__':
    get_colors()
# result = device.screencap()
# with open("red.png", "wb") as fp:
#     fp.write(result)
    