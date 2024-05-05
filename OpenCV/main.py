import cv2 as cv
import numpy as np
import os
from time import time
from time import sleep
from windowcapture import WindowCapture
import pyautogui
import state_machine
import debug_logging as log
"""*********************************************************************
*! \fn          main
*  \brief       start code
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""


"""*********************************************************************
                Constant
*********************************************************************"""
#without chat
pos_dock1_no_chat = (750, 950)
region_dock1_no_chat = (650,910,90,110)
pos_attack_btn_no_chat = (1300, 600)
pos_location_btn_no_chat = (100, 910)
pos_close_chat_btn = (500,20)

"""*********************************************************************
                local val
*********************************************************************"""
current_state = "init"
next_state = "init"
"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def move_mouse(target_pos):
    screen_x, screen_y = wincap.get_screen_position(target_pos)
    # print('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # print('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(x=screen_x - 51, y=screen_y + 11)
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(0.5)
    pyautogui.mouseUp()

def move_mouse_click(target_pos):
    screen_x, screen_y = wincap.get_screen_position(target_pos)
    # print('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # print('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(x=screen_x, y=screen_y)
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(0.5)
    pyautogui.mouseUp()

"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
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

__name__ == '__main__'

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the Vision class
wincap = WindowCapture('Star Trek Fleet Command')

#wincap.saveRegion(region_dock1_no_chat)
#sleep(30)


#start state machine
while(True):

    wincap.saveScreenShot()
    current_state = next_state
    log.debug_msg("state is " + current_state)
    match current_state:
        case "init":
            #check if chat active.
            pos = confirm_screen('currentscreen.png', './picture/chat_on_right_side.png', 0.17)
            if pos:
                log.debug_msg("chat open")
                pos = confirm_screen('currentscreen.png', './picture/chat_side_close.png', 0.17)
                move_mouse_click(pos[0])
            else:
                log.debug_msg("chat close")
                next_state = "select_ship"
        case "select_ship":
            move_mouse(pos_dock1_no_chat)
            sleep(1);
            move_mouse(pos_location_btn_no_chat)
            next_state = "find_target"
        case _:
            log.debug_msg("default_state")
    sleep(10)


loop_time = time()
while(True):

    # get an updated image of the game
    #screenshot2 = wincap.get_screenshot()
    #screenshot = wincap.saveScreenShot()

    # select ship
    move_mouse(pos_dock1_no_chat)

    ###################### search taget ####################################################

    screenshot = wincap.saveScreenShot()
    current_screen_image = cv.imread('currentscreen.png', cv.IMREAD_COLOR )
    hostile_image = cv.imread('./picture/miner.png', cv.IMREAD_COLOR)
    result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
    threshold = 0.17
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))
    #print(locations)

    if locations:
        print('hostiles needle.')
        hostile_w = hostile_image.shape[1]
        hostile_h = hostile_image.shape[0]
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        # Loop over all the locations and draw their rectangle
        for loc in locations:
            # Determine the box positions
            top_left = loc
            bottom_right = (top_left[0] + hostile_w, top_left[1] + hostile_h)
            # Draw the box
            cv.rectangle(current_screen_image, top_left, bottom_right, line_color, line_type)
        #sore result image
        cv.imwrite('result.jpg', current_screen_image)

    else:
        print('Needle not found.')

    #click
    target_pos = locations[0]
    move_mouse(target_pos)
    # short pause to let the mouse movement complete and allow


    ################### confirm click ########################

    screenshot = wincap.saveScreenShot()
    #current_screen_image = cv.imread('currentscreen.png', cv.IMREAD_COLOR)
    #hostile_image = cv.imread('./picture/confirm_miner.png', cv.IMREAD_COLOR)
    #result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
    #threshold = 0.17
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    #locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    #locations = list(zip(*locations[::-1]))
    #print(locations)

    if confirm_screen('currentscreen.png', './picture/confirm_miner.png', 0.17):
        print("confirmed")

        #check if ship in region
        current_screen_image = cv.imread('currentscreen.png', cv.IMREAD_COLOR)
        hostile_image = cv.imread('./picture/attack_ready.png', cv.IMREAD_COLOR)
        result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
        threshold = 0.17
        atk_btn_locations = np.where(result <= threshold)
        atk_btn_locations = list(zip(*atk_btn_locations[::-1]))
        if atk_btn_locations:
            print ("attack")
            move_mouse(pos_attack_btn_no_chat)


    else:
        print("no target")


    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    sleep(30)


print('Done.')