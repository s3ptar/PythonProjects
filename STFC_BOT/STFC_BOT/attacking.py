"""*********************************************************************
*! \file:                   debug_logging
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
import json
import pyautogui
from time import sleep
from pywinauto import keyboard
import numpy as np
from windowcapture import WindowCapture
import cv2 as cv
import logging_lib
"""*********************************************************************
* Informations
*********************************************************************"""
# https://os.mbed.com/platforms/FRDM-K64F/#board-pinout
"""*********************************************************************
* Declarations
*********************************************************************"""

"""*********************************************************************
* Constant
*********************************************************************"""
delay_click = 0.2
mouse_pos_top = (600,10)
region_allianz_btn = (5,900,100,100)
region_ship_properties_repair = (5,900,100,60)
offset_y = 11
offset_x = -51
#repair_speed_up_pos = (1100,580)
repair_speed_up_pos = (1157,491)
searchinput_field_pos = (800,450)
systemname_field_pos = (800,100)
pos_location_btn_no_chat = (100, 910)
pos_attack_btn_no_chat = (1300, 600)
region_dock1_no_chat = (670,910,90,110)
region_ship_number = (60,640, 150,100)
""""*********************************************************************
* Global Variable
*********************************************************************"""
wincap = WindowCapture('Star Trek Fleet Command')
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
*! \fn          check_miss_clicks(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def check_miss_clicks():
    #pos = confirm_screen("./picture/missclick/holo_esc.png", 0.1)
    #if pos:
    keyboard.send_keys('{ESC}')


"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def confirm_screen(search_img, threshold, debug_enable=1):

    current_screen_image = wincap.saveScreenShot(debug_enable)
    hostile_image = cv.imread(search_img, cv.IMREAD_COLOR)
    result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
    #threshold = 0.17
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))

    if debug_enable:
        if locations:
            needle_w = hostile_image.shape[1]
            needle_h = hostile_image.shape[0]
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            # Loop over all the locations and draw their rectangle
            for loc in locations:
                # Determine the box positions
                top_left = loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
                # Draw the box
                cv.rectangle(current_screen_image, top_left, bottom_right, line_color, line_type)
            cv.imwrite("debug\confirm_screen_debug.png", current_screen_image)

    return locations

"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def confirm_screen_grey(search_img, threshold, debug_enable=1):
    lower = np.array([155, 25, 0])
    upper = np.array([179, 255, 255])


    #threshold = 0.2
    current_screen_image = wincap.saveScreenShot(debug_enable)
    image = cv.cvtColor(current_screen_image, cv.COLOR_BGR2HSV)

    mask = cv.inRange(image, lower, upper)
    current_screen_image = cv.bitwise_and(current_screen_image, current_screen_image, mask=mask)
    #hostile_image = cv.imread(search_img, cv.IMREAD_GRAYSCALE)
    #current_screen_image = cv.cvtColor(current_screen_image, cv.COLOR_BGR2GRAY)

    hostile_image = cv.imread(search_img, cv.IMREAD_COLOR)
    image = cv.cvtColor(hostile_image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(image, lower, upper)
    hostile_image = cv.bitwise_and(hostile_image, hostile_image, mask=mask)


    cv.imwrite("debug\confirm_screen_grey_screen_debug.png", current_screen_image)
    cv.imwrite("debug\confirm_screen_grey_search_debug.png", hostile_image)

    result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
    #threshold = 0.17
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))

    if debug_enable:
        if locations:
            needle_w = hostile_image.shape[1]
            needle_h = hostile_image.shape[0]
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            # Loop over all the locations and draw their rectangle
            for loc in locations:
                # Determine the box positions
                top_left = loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
                # Draw the box
                cv.rectangle(current_screen_image, top_left, bottom_right, line_color, line_type)
            cv.imwrite("debug\confirm_screen_grey_debug.png", current_screen_image)

    return locations

"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def confirm_region(search_img, threshold, region, debug_enable=1):

    #current_screen_image = cv.imread(basic_img, cv.IMREAD_COLOR)

    current_screen_image = wincap.saveRegion(region)
    hostile_image = cv.imread(search_img, cv.IMREAD_COLOR)
    result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
    #threshold = 0.17
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))

    if debug_enable:
        if locations:
            needle_w = hostile_image.shape[1]
            needle_h = hostile_image.shape[0]
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            # Loop over all the locations and draw their rectangle
            for loc in locations:
                # Determine the box positions
                top_left = loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
                # Draw the box
                cv.rectangle(current_screen_image, top_left, bottom_right, line_color, line_type)
            cv.imwrite("debug\confirm_screen_debug.png", current_screen_image)

    return locations


"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def move_mouse(target, x_offset=0, y_offset=0):
    #screen_x, screen_y = wincap.get_screen_position(target_pos)
    # debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(target[0]+x_offset, target[1]+y_offset)
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(delay_click)
    pyautogui.mouseUp()
    sleep(delay_click)

"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def move_mouse_position(target_pos, x_offset=0, y_offset=0):
    screen_x, screen_y = wincap.get_screen_position(target_pos)
    # log.debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # log.debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(x=screen_x + x_offset, y=screen_y + y_offset)
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
def move_mouse_click(target):
    #screen_x, screen_y = wincap.get_screen_position(target_pos)
    # debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(target.x, target.y)
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(delay_click)
    pyautogui.mouseUp()

"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def nav_send_short_cut(target, cmd):
    pyautogui.moveTo(target[0], target[1])
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(delay_click)
    pyautogui.mouseUp()
    sleep(delay_click)
    keyboard.send_keys('{VK_SPACE}')


"""*********************************************************************
*! \fn          select_dock(dock_num):
*  \brief       select specified dock and open ship properties
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def select_dock(dock_num):
    move_mouse(mouse_pos_top)
    if dock_num == 1:
        #chec if ship a is select
        if not confirm_region("./picture/schiff_A.png", 0.1, region_ship_number, 1):
            keyboard.send_keys('%1')
    sleep(delay_click)
    #if confirm_region("./picture/allianz_btn_logo.png", 0.1, region_allianz_btn,1):
    #    #check if ship menu open, if not send another cmd
    #    if dock_num == 1:
    #        keyboard.send_keys('%1')




"""*********************************************************************
*! \fn          wait_unilt_ship_rdy(dock)
*  \brief       wait until ship stop moving
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def wait_unilt_ship_rdy(dock):

    select_dock(dock)
    loop_condition = 1
    return_value = 0

    if confirm_screen('./picture/dock_state_schiff_wartet.png', 0.01,1):
        loop_condition = 0
        return_value = 1
    if confirm_screen('./picture/dock_state_repair_btn.png', 0.01,1):
        loop_condition = 0
        return_value = 2
    if confirm_screen('./picture/dock_state_destroyed.png', 0.01,1):
        loop_condition = 0
        return_value = 3
    sleep(1)

    #Dock 1 abwählen
    #keyboard.send_keys('%1')
    #center schiff
    #keyboard.send_keys('{SPACE}')
    #keyboard.send_keys('%')
    #print("schiff stop moving")
    return return_value

"""*********************************************************************
*! \fn          prepare_attacking(dock)
*  \brief       preapare attakscreen
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def prepare_attacking():
    pos = confirm_screen('./picture/battlescrren.png', 0.07)
    #battle screen aktivieren falls nicht schon aktiviert
    if pos:
        move_mouse_position((1878,855))
        #keyboard.send_keys('%shift')
    move_mouse_position((224,202))
    sleep(1)
    pyautogui.scroll(-8000)  # scroll out
    return

def test_log():
    logging_lib.logging_msg(msg="test")

"""*********************************************************************
*! \fn          attacking(target_setup, next_target)
*  \brief       attaking until task empty
*  \param       target_list - list with target classes
*  \param       next_target - default enable, if 0 jump over closed target calc
*  \exception   none
*  \return      none
*********************************************************************"""
def attacking(target_list, next_target = 1, threshold = 0.1):
    try:
        prepare_attacking()
        target_class = 0
        target_pos = 9999999999
        result_locs = list()

        target_data = target_list[0]

        #check if battle mode enabled

        if next_target:
            target_pos = 9999999999
        else:
            target_pos = 0

        ship_pos = confirm_screen('./picture/ship_dock_a.png', 0.1)
        if ship_pos:
            ship_pos = confirm_screen('./picture/ship_dock_a.png', 0.1)
        else:
            ship_pos = [(960, 540)]

        distance = 99999999999999

        if target_data['battleship'] > 0:
            # battleships
            pos = confirm_screen_grey('./picture/hostiles/battleship.png', threshold, )
            if next_target:

                loop_index = 0

                if pos:
                    """distance = np.sqrt((np.square(ship_pos[0][0] - pos[0][0])) +
                                                   (np.square(ship_pos[0][1] - pos[0][1])))"""
                    # found closed spot
                    for loc in pos:
                        next_target = np.sqrt((np.square(ship_pos[0][0] - loc[0])) +
                                              (np.square(ship_pos[0][1] - loc[1])))

                        if distance > next_target:
                            distance = next_target
                            closed_target_pos = loop_index
                            target_pos = pos[loop_index]
                            target_class = "battleship"
                        loop_index = loop_index + 1
            else:
                if not target_pos and pos:
                    target_pos = pos[0]
                    target_class = "battleship"

        if target_data['interceptor'] > 0:
            # interceptor

            pos = confirm_screen_grey('./picture/hostiles/interceptor.png', threshold, )
            if next_target:
                loop_index = 0

                if pos:
                    """distance = np.sqrt((np.square(ship_pos[0][0] - pos[0][0])) +
                                       (np.square(ship_pos[0][1] - pos[0][1])))"""
                    # found closed spot
                    for loc in pos:
                        next_target = np.sqrt((np.square(ship_pos[0][0] - loc[0])) +
                                              (np.square(ship_pos[0][1] - loc[1])))

                        if distance > next_target:
                            distance = next_target
                            closed_target_pos = loop_index
                            target_pos = pos[loop_index]
                            target_class = "interceptor"
                        loop_index = loop_index + 1
            else:
                if not target_pos and pos:
                    target_pos = pos[0]
                    target_class = "interceptor"

        if target_data['explorer'] > 0:
            # science
            pos = confirm_screen_grey('./picture/hostiles/science.png', threshold )
            if next_target:
                loop_index = 0

                if pos:
                    """distance = np.sqrt((np.square(ship_pos[0][0] - pos[0][0])) +
                                       (np.square(ship_pos[0][1] - pos[0][1])))"""
                    # found closed spot
                    for loc in pos:
                        next_target = np.sqrt((np.square(ship_pos[0][0] - loc[0])) +
                                              (np.square(ship_pos[0][1] - loc[1])))

                        if distance > next_target:
                            distance = next_target
                            closed_target_pos = loop_index
                            target_pos = pos[loop_index]
                            target_class = "science"
                        loop_index = loop_index + 1
                else:
                    if not target_pos:
                        target_pos = pos[0]
                        target_class = "science"

                #move_mouse_position(target_pos,-20)

        if target_data['miner'] > 0:
            # miner
            pos = confirm_screen_grey('./picture/hostiles/miner.png', threshold)
            if next_target:
                loop_index = 0
                if pos:
                    """distance = np.sqrt((np.square(ship_pos[0][0] - pos[0][0])) +
                                                   (np.square(ship_pos[0][1] - pos[0][1])))"""
                    # found closed spot
                    for loc in pos:
                        next_target = np.sqrt((np.square(ship_pos[0][0] - loc[0])) +
                                              (np.square(ship_pos[0][1] - loc[1])))

                        if distance > next_target:
                            distance = next_target
                            target_pos = pos[loop_index]
                            target_class = "miner"
                        loop_index = loop_index + 1
            else:
                if not target_pos and pos:
                    target_pos = pos[0]
                    target_class = "miner"

        #select target in the allowed windows
        if (target_pos and (target_pos[1] > 110) and (target_pos[1] < 900) and (target_pos[0] > 183) and
                (target_pos[0] < 1684)):
            move_mouse_position(target_pos, -35, +3)
        else:
            return 0
        if target_class == "battleship":
            confirm_path = './picture/hostiles/confirm_battleship.png'
        elif target_class == "interceptor":
            confirm_path = './picture/hostiles/confirm_interceptor.png'
        elif target_class == "science":
            confirm_path = './picture/hostiles/confirm_science.png'
        elif target_class == "miner":
            confirm_path = './picture/hostiles/confirm_miner.png'
        else:
            #print("no target")
            return 0
        #check target and attcack
        pos = confirm_screen(confirm_path, 0.1, )
        if pos:
            #pos = confirm_screen('./picture/attack_ready.png', 0.1, )
            move_mouse_position((1287,635))
            return 1
    except:
        #print("An exception occurred in attacking")
        return 0


"""*********************************************************************
*! \fn          check_ship(dock)
*  \brief       check ship status. if full cargo send home
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def check_ship(dock):
    pos = confirm_region('./picture/cargo_full.png', 0.17, region_dock1_no_chat)
    if pos:
        # send home
        keyboard.send_keys('%m')
        return 1
    else:
        return 0