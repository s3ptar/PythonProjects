import cv2
import numpy as np
import os
from time import time
from time import sleep
from windowcapture import WindowCapture


# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Star Trek Fleet Command')
# initialize the Vision class
 


loop_time = time()
while(True):

    # get an updated image of the game
    wincap = WindowCapture('Star Trek Fleet Command')
    screenshot = wincap.get_screenshot()

   # cv2.imshow('Computer Vision', screenshot)
    cv2.imwrite('D:\Repos\PythonProjects\OpenCV\Screenshot.png', screenshot)
    screenshot = 0
    

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    sleep(5)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses


print('Done.')