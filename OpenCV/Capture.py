# -*- coding: utf-8 -*-

"""*********************************************************************
*! \file:                   capture.py
*  \projekt:                GameBot
*  \created on:             2024 02 21
*  \author:                 R. Gräber
*  \version:                0
*  \history:                -
*  \brief
*********************************************************************"""


"""*********************************************************************
* Includes
*********************************************************************"""


import numpy as np
import win32gui, win32ui, win32con
import json


"""*********************************************************************
* Declarations
*********************************************************************"""


"""*********************************************************************
* Constant
*********************************************************************"""


"""*********************************************************************
* Global Variable
*********************************************************************"""


"""*********************************************************************
* local Variable
*********************************************************************"""

"""*********************************************************************
* Constant
*********************************************************************"""

"""*********************************************************************
* Local Funtions
*********************************************************************"""



"""*********************************************************************
*! \fn          class WindowsCapture
*  \brief       class constructor
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""

class WinCap:

    # properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    
    # constructor
    def __init__(self, window_name=None):
        # find the handle for the window we want to capture.
        # if no window name is given, capture the entire screen
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))

        self.get_screen_porperties()
        
    """*********************************************************************
    *! \fn          get_screen_porperties(self)
    *  \brief       refresh window propetieis
    *  \param       none
    *  \exception   none
    *  \return      none
    *********************************************************************"""
        
    def get_screen_porperties(self):
        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]


        # account for the window border and titlebar and cut them off
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels

        
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels
        

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y
