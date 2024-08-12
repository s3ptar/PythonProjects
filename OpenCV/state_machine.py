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

import pyautogui
import cv2 as cv
import numpy as np
from windowcapture import WindowCapture
import debug_logging as log
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
wincap = WindowCapture('Star Trek Fleet Command')
last_target_pos = 0
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
pos_battle_screen_btn = (1800,700)
ship_last_pos = [(500,20)]
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
def move_mouse(target_pos):
    screen_x, screen_y = wincap.get_screen_position(target_pos)
    # log.debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # log.debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(x=screen_x - 51, y=screen_y + 11)
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(0.5)
    pyautogui.mouseUp()

def move_mouse_click(target_pos,x_offset = 0, y_offset = 0):
    screen_x, screen_y = wincap.get_screen_position(target_pos)
    # log.debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # log.debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(x=screen_x+x_offset, y=screen_y+y_offset)
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
def confirm_screen(basic_img, search_img, threshold, debug_enable=0):

    #current_screen_image = cv.imread(basic_img, cv.IMREAD_COLOR)
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
            cv.imwrite("currentregion_debug.png", current_screen_image)
        else:
            log.debug_msg("no locations")

    return locations


"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def confirm_region(basic_img, search_img, threshold, region, debug_enable=0):

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
            cv.imwrite("currentregion_debug.png", current_screen_image)

    return locations


"""*********************************************************************
*! \fn          send_to_system(system)
*  \brief       send ship to system
*  \param       system name
*  \exception   none
*  \return      none
*********************************************************************"""
def send_to_system(system_name):
    #wincap.saveScreenShot()
    pos = confirm_screen('currentscreen.png', './picture/bookmark_systems.png', 0.05)
    move_mouse(pos[0])
    sleep(0.5)
    wincap.saveScreenShot()
    pos = confirm_screen('currentscreen.png', './picture/system_search.png', 0.17)
    move_mouse(pos[0])
    sleep(0.5)
    wincap.saveScreenShot()
    pos = confirm_screen('currentscreen.png', './picture/system_search_input.png', 0.05)
    move_mouse_click(pos[0])
    sleep(0.5)
    wincap.saveScreenShot()
    pos = confirm_screen('currentscreen.png', './picture/insert_system_name.png', 0.17)
    move_mouse_click(pos[0], 80, 10)
    sleep(0.5)
    pyautogui.write(system_name)
    wincap.saveScreenShot()
    system_path = './picture/systems/' + system_name + '.png'
    system_path = system_path.replace(" ", "_")
    pos = confirm_screen('currentscreen.png', system_path, 0.01)
    move_mouse_click(pos[0])
    sleep(0.5)
    wincap.saveScreenShot()
    pos = confirm_screen('currentscreen.png', './picture/los_btn.png', 0.17)
    move_mouse_click(pos[0])
    sleep(0.5)
    #zoom in
    pyautogui.scroll(-10)  # scroll down 10 "clicks"

    # check screen
    wincap.saveScreenShot()
    confirm_path = './picture/systems/' + system_name + '_confirm.png'
    confirm_path = confirm_path.replace(" ", "_")
    pos = confirm_screen('currentscreen.png', confirm_path, 0.17)
    if pos:
        # send outer system
        move_mouse_click(pos[0])
        sleep(0.5)
        wincap.saveScreenShot()

        # added token systems
        pos = confirm_screen('currentscreen.png', './picture/setze_kurs.png', 0.17)
        if pos:
            move_mouse_click(pos[0])
        else:
            # is token system
            pos = confirm_screen('currentscreen.png', './picture/setze_kurs_token.png', 0.17)
            move_mouse_click(pos[0])
            pos = confirm_screen('currentscreen.png', './picture/setze_kurs_token_route.png', 0.17)
            move_mouse_click(pos[0])
    else:
        # send inner system
        move_mouse_click((800, 500))
        #wincap.saveScreenShot()
        pos = confirm_screen('currentscreen.png', './picture/nicht_im_system.png', 0.17)
        if pos:
            move_mouse_click(pos[0], 20, 25)
            #check token system
            wincap.saveScreenShot()
            pos = confirm_screen('currentscreen.png', './picture/setze_kurs_token_route.png', 0.17)
            if pos:
                move_mouse_click(pos[0])

        else:
            #new click
            move_mouse_click((820, 490))
            pos = confirm_screen('currentscreen.png', './picture/nicht_im_system.png', 0.17)
            if pos:
                move_mouse_click(pos[0], 20, 25)
            else:
                return



"""*********************************************************************
*! \fn          def get_target(target_list)
*  \brief       find target
*  \param       system name
*  \exception   none
*  \return      none
*********************************************************************"""
def attack_target(target_list):
    #move_mouse_click(1000,500)
    #pyautogui.scroll(+10)  # scroll up 10 "clicks"
    hostile_image = []
    closed_target_pos = 0
    result = 0
    result_locs = list()
    current_screen_image = wincap.saveScreenShot(debug_enable=1)
    if target_list[0] > 0:
        #battleships
        hostile_image = cv.imread('./picture/hostiles/battleship.png', cv.IMREAD_COLOR)
        result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
        threshold = 0.1
        locations = np.where(result <= threshold)
        result_locs += list((zip(*locations[::-1])))
    if target_list[1] > 0:
        #interceptor
        hostile_image =  cv.imread('./picture/hostiles/interceptor.png', cv.IMREAD_COLOR)
        result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
        threshold = 0.1
        locations = np.where(result <= threshold)
        result_locs += list((zip(*locations[::-1])))
    if target_list[2] > 0:
        #science
        hostile_image = cv.imread('./picture/hostiles/science.png', cv.IMREAD_COLOR)
        result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
        threshold = 0.1
        locations = np.where(result <= threshold)
        result_locs += list((zip(*locations[::-1])))
    if target_list[3] > 0:
        #miner
        hostile_image = cv.imread('./picture/hostiles/miner.png', cv.IMREAD_COLOR)
        result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
        threshold = 0.1
        locations = np.where(result <= threshold)
        result_locs += list((zip(*locations[::-1])))

    #result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
    ##threshold = 0.1
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    ##locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    ##locations = list(zip(*locations[::-1]))
    # log.debug_msg(locations

    #find closed spot

    loop_index = 0
    #center ship
    ship_pos = confirm_screen("egal", './picture/ship_dock_a.png', 0.1)
    if ship_pos:
        ship_pos = confirm_screen("egal", './picture/ship_dock_a.png', 0.1)
    else:
        ship_pos = [(960,540)]
    distance = 0
    # click
    if result_locs:
        try:
            distance = np.sqrt((np.square(ship_pos[0][0] - result_locs[0][0])) +
                               (np.square(ship_pos[0][1] - result_locs[0][1])))
            # found closed spot
            for loc in result_locs:
                next_target = np.sqrt((np.square(ship_pos[0][0] - loc[0])) +
                                      (np.square(ship_pos[0][1] - loc[1])))
                loop_index = loop_index + 1
                if distance > next_target:
                    distance = next_target
                    closed_target_pos = loop_index

            target_pos = result_locs[closed_target_pos]
            move_mouse(target_pos)
        except:
            log.debug_msg("no target")
            return 0
    else:
        log.debug_msg("no target")
        return 0
    # short pause to let the mouse movement complete and allow
    ################### confirm click ########################
    #screenshot = wincap.saveScreenShot()
    # current_screen_image = cv.imread('currentscreen.png', cv.IMREAD_COLOR)
    # hostile_image = cv.imread('./picture/confirm_miner.png', cv.IMREAD_COLOR)
    # result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
    # threshold = 0.17
    # The np.where() return value will look like this:
    # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    # locations = np.where(result <= threshold)
    # We can zip those up into a list of (x, y) position tuples
    # locations = list(zip(*locations[::-1]))
    #log.debug_msg(locations)
    confirm_path = './picture/hostiles/empty.png'
    if target_list[0] > 0:
        #battleships
        if confirm_screen('currentscreen.png', './picture/hostiles/confirm_battleship.png', 0.17):
            confirm_path = './picture/hostiles/confirm_battleship.png'
    elif target_list[1] > 0:
        #interceptor
        if confirm_screen('currentscreen.png', './picture/hostiles/confirm_interceptor.png', 0.17):
            confirm_path = './picture/hostiles/confirm_interceptor.png'
    elif target_list[2] > 0:
        #science
        if confirm_screen('currentscreen.png', './picture/hostiles/confirm_science.png', 0.17):
            confirm_path = './picture/hostiles/confirm_science.png'
    elif target_list[3] > 0:
        #miners
        if confirm_screen('currentscreen.png', './picture/hostiles/confirm_miner.png', 0.17):
            confirm_path = './picture/hostiles/confirm_miner.png'
    else:
        return 0
    #wincap.saveScreenShot()
    if confirm_screen('currentscreen.png', confirm_path, 0.17) :

        # check if ship in region
        current_screen_image = wincap.saveScreenShot()
        hostile_image = cv.imread('./picture/attack_ready.png', cv.IMREAD_COLOR)

        result = cv.matchTemplate(current_screen_image, hostile_image, cv.TM_SQDIFF_NORMED)
        threshold = 0.17
        atk_btn_locations = np.where(result <= threshold)
        atk_btn_locations = list(zip(*atk_btn_locations[::-1]))
        if atk_btn_locations:
            move_mouse(pos_attack_btn_no_chat)
            return 1

    else:
        log.debug_msg("no target")
        return 0