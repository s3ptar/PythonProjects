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
from subprocess import call
import threading
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
pos_system_ok_btn = (1335, 140)
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
*! \fn          select_dock(dock_num):
*  \brief       select specified dock and open ship properties
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def close_chat_window():
    #check if ship need repair
    move_mouse(mouse_pos_top)
    pos = confirm_screen("./picture/chat_side_close.png", 0.1)
    if pos:
        #print("close chat windows")
        move_mouse_position(pos[0])

"""*********************************************************************
*! \fn          select_dock(dock_num):
*  \brief       select specified dock and open ship properties
*  \param       dock - num of doc
*  \param       repair_first_time, if first time rep
*  \exception   none
*  \return      none
*********************************************************************"""
def repair_ship(dock, repair_first_time):
    repair_need = 0
    return_value = 0
    keyboard.send_keys('%m')
    #keyboard.send_keys('{VK_F2}')
    if not repair_first_time:
        select_dock(dock)
        sleep(2)
    #check if ship need repair
    ##move_mouse(mouse_pos_top)
    #hit repair button if exists
    #print ("check repair")
    select_dock(dock)
    pos = confirm_screen("./picture/dock_state_repair_btn.png", 0.01,1)
    if pos:
        move_mouse_position(pos[0])
        # repair_need = 1
        return 0

    pos = confirm_screen("./picture/gratis_repair.png", 0.1)
    if pos:
        move_mouse_position(pos[0])
        return 1

    pos = confirm_screen("./picture/gratis_repair_5min.png", 0.1,1)
    if pos:
        move_mouse_position(pos[0])
        return 1

    pos = confirm_screen("./picture/hilfe_btn.png", 0.01)
    if pos:
        move_mouse_position(pos[0])
        # repair_need = 1
        return 0

    # hit speed button if exists
    pos = confirm_screen("./picture/beschleunigen_btn.png", 0.01,1)
    if pos:
        move_mouse_position(pos[0])
        # repair_need = 1
        return 0

    # check gratis repair
    pos = confirm_screen("./picture/int_repair_speed_up.png", 0.1)
    if pos:
        move_mouse_position(pos[0])
        return 0

    #check gratis repair
    pos = confirm_screen("./picture/repair_speed_up_okay.png", 0.1)
    if pos:
        move_mouse_position(pos[0])
        return 0

    pos = confirm_screen("./picture/repair_done.png", 0.05, 1)
    if not pos:
        move_mouse_position(repair_speed_up_pos)
        return 0

    pos = confirm_screen("./picture/dock_state_ship_in_dock.png", 0.05, 1)
    if pos:
        return 1

    return 0



"""*********************************************************************
*! \fn          send_to_system():sn
*  \brief       select specified dock and open ship properties
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def send_to_system(system_name, dock):

    #bookmark
    move_mouse_position((1826,878))

    sleep(2)
    #systgem search
    move_mouse_position((1732, 102))
    sleep(2)
    # enter system name and click
    move_mouse_position((972, 484))
    sleep(2)
    move_mouse_position((943, 132))
    sleep(2)
    pyautogui.write(system_name)
    sleep(2)
    #system_path = './picture/systems/' + system_name + '.png'
    #system_path = system_path.replace(" ", "_")
    #pos = confirm_screen(system_path, 0.09,1)
    #if not pos:
    #    return 0
    #move_mouse_position(pos[0])
    move_mouse_position(pos_system_ok_btn)
    sleep(2)
    # click los button
    move_mouse_position((1001,1007))
    sleep(2)
    #check if tiken

    #scroll down
    pyautogui.scroll(+8000)  # scroll out
    sleep(0.5)
    #click system
    move_mouse_position((960, 519))
    sleep(0.5)
    pos = confirm_screen('./picture/setze_kurs.png', 0.01,1 )
    if pos:
        move_mouse_position(pos[0])
        #check gorn
        pos = confirm_screen('./picture/setze_kurs_gon.png', 0.01)
        if pos:
            move_mouse_position(pos[0])
        return 1
        #no token systen. send to bekannte systeme
    #move_mouse_position((800, 500))
    pos = confirm_screen('./picture/nicht_im_system.png', 0.17)
    if pos:
        move_mouse_position(pos[0])
        # check token system
        wincap.saveScreenShot()
        pos = confirm_screen('./picture/setze_kurs_token_route.png', 0.17)
        if pos:
            move_mouse_position(pos[0])
        return 1

    else:
        # new click
        # token system
        #move_mouse_position((820, 490))
        #pos = confirm_screen( './picture/nicht_im_system.png', 0.17)
        pos = confirm_screen('./picture/setze_kurs_toekn.png', 0.17)
        if pos:
            move_mouse_position(pos[0])
            pos = confirm_screen('./picture/setze_kurs_token_route.png', 0.17)
            if pos:
                move_mouse_position(pos[0])
                pos = confirm_screen('./picture/setze_kurs_token_route.png', 0.17)
                if pos:
                    move_mouse_position(pos[0])
            return 1
        else:
            return 1


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
    if confirm_screen('./picture/dock_state_ship_in_dock.png', 0.01,1):
        loop_condition = 0
        return_value = 99
    sleep(1)

    #Dock 1 abwählen
    #keyboard.send_keys('%1')
    #center schiff
    keyboard.send_keys('{SPACE}')
    #keyboard.send_keys('%')
    #print("schiff stop moving")
    return return_value


"""*********************************************************************
*! \fn          check_ship(dock)
*  \brief       check ship status. if full cargo send home
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def check_ship(dock, check_cargo_full):
    if check_cargo_full==0:
        return 0
    pos = confirm_region('./picture/cargo_full.png', 0.17, region_dock1_no_chat)
    if pos:
        # send home
        keyboard.send_keys('%m')
        return 1
    else:
        return 0


"""*********************************************************************
*! \fn          restart_game()
*  \brief       restat game
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""

def restart_game():
    close_game()
    x = threading.Thread(target=start_game, args=())
    x.start()
    sleep(120)
    pos = confirm_screen('./picture/missclick/timeout_after_restart.png', 0.17)
    if pos:
        pos = confirm_screen('./picture/missclick/quittierung_timeout.png', 0.17)
        if pos:
            move_mouse_position(pos[0])

"""*********************************************************************
*! \fn          close_game()
*  \brief       restat game
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def close_game():
    move_mouse_position((1899,12),y_offset=-30)
    sleep(60)

"""*********************************************************************
*! \fn          start_game()
*  \brief       start game
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def start_game():
    call(r"C:\Games\Star Trek Fleet Command\STFC\default\game\prime.exe")