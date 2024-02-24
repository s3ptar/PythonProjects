# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:15:35 2024

@author: rene_


"""

import cv2
import win32gui, win32ui, win32con
from PIL import ImageGrab

def capture_dynamic():
    toplist, winlist = [], []
    
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
        
    win32gui.EnumWindows(enum_cb, toplist)

    wnd = [(hwnd, title) for hwnd, title in winlist if 'Star Trek Fleet Command' in title.lower()]

    if wnd:
        wnd = wnd[0]
        hwnd = wnd[0]

        bbox = win32gui.GetWindowRect(hwnd)
        img = ImageGrab.grab(bbox)
        return img
    else:
        return None
    
    
capture_dynamic()