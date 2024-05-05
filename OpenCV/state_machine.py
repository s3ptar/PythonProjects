"""*********************************************************************
*! \file:                   state_machine
*  \projekt:                game_bot
*  \created on:             2024 05 09
*  \author:                 R. Gräber
*  \version:                0
*  \history:                -
*  \brief                   host state maschine
*********************************************************************"""


"""*********************************************************************
* Includes
*********************************************************************"""
from time import sleep
import debug_logging
import pyautogui
import cv2 as cv
import numpy as np
"""*********************************************************************
* Informations
*********************************************************************"""
#https://os.mbed.com/platforms/FRDM-K64F/#board-pinout
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
pos_dock1_no_chat = (750, 950)
region_dock1_no_chat = (650,910,90,110)
pos_attack_btn_no_chat = (1300, 600)
pos_location_btn_no_chat = (100, 910)
pos_close_chat_btn = (500,20)
"""*********************************************************************
* Local Funtions
*********************************************************************"""

"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def move_mouse(wincap ,target_pos):
    screen_x, screen_y = wincap.get_screen_position(target_pos)
    pyautogui.moveTo(x=screen_x - 51, y=screen_y + 11)
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(0.5)
    pyautogui.mouseUp()

"""*********************************************************************
*! \fn          confirm_screen(basic_img, search_img, threshold):
*  \brief       compare picture
*  \param       basic_img - capture image
*  \param       search_img - search image
*  \param       threshold 
*  \exception   none
*  \return      location
*********************************************************************"""
def confirm_screen(basic_img, search_img, threshold):
    current_screen_image = cv.imread(basic_img, cv.IMREAD_COLOR)
    hostile_image = cv.imread(search_img, cv.IMREAD_COLOR)
    result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
    #threshold = 0.17
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))
    return locations

"""*********************************************************************
*! \fn          int main(){
*  \brief       start up function
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def check_chat_window(wincap):
    print("dd")