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
pos_recall_btn_no_chat = (100, 980)
pos_close_chat_btn = (500,20)
pos_repair_screen_btn = (1200,540)

pos_battle_screen_btn = (1860,850)

dummy = 0

"""*********************************************************************
                local val
*********************************************************************"""
current_state = "init"
next_state = "init"
target_count = 0
enable_battle_screen = 0
#0 = until full cargo
num_of_targets = 0
#target_system = "beta-sektor"
target_system = "neara"
#1 battleship
#2 int
#3 science
#4 miner
target_class = [1,1,1,1]
#target_class = [0,0,1,0]
"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def move_mouse(target_pos):
    screen_x, screen_y = wincap.get_screen_position(target_pos)
    # debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(x=screen_x - 51, y=screen_y + 11)
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(0.5)
    pyautogui.mouseUp()

def move_mouse_click(target_pos,x_offset = 0, y_offset = 0):
    screen_x, screen_y = wincap.get_screen_position(target_pos)
    # debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # debug_msg('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))
    # move the mouse
    pyautogui.moveTo(x=screen_x+x_offset, y=screen_y+y_offset)
    pyautogui.mouseDown()
    pyautogui.click()
    sleep(0.5)
    pyautogui.mouseUp()



__name__ == '__main__'

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the Vision class
wincap = WindowCapture('Star Trek Fleet Command')

#wincap.saveRegion(region_dock1_no_chat)
#move_mouse_click((1200,540))
#sleep(200)


#start state machine
while(True):

    #wincap.saveScreenShot()
    current_state = next_state
    log.debug_msg("state is " + current_state)
    match current_state:
        case "init":
            #check if chat active.
            pos = state_machine.confirm_screen('currentscreen.png', './picture/chat_on_right_side.png', 0.17)
            if pos:
                log.debug_msg("chat window is open")
                pos = state_machine.confirm_screen('currentscreen.png', './picture/chat_side_close.png', 0.17)
                move_mouse_click(pos[0])
            else:
                log.debug_msg("chat window closed")
                next_state = "select_ship"
        case "select_ship":
            move_mouse((100,700))
            log.debug_msg("select ship")
            move_mouse(pos_dock1_no_chat)
            sleep(0.5)
            if state_machine.confirm_screen('currentscreen.png', './picture/schiff_verwaltung.png', 0.17):
                dummy = 0
            else:
                move_mouse(pos_dock1_no_chat)
            move_mouse(pos_location_btn_no_chat)
            next_state = "send_system"
        case "send_system":
            target_count = 0
            state_machine.send_to_system(target_system)
            log.debug_msg("send to system")
            next_state = "wait_for_arrive"
        case "wait_for_arrive":
            #wincap.saveRegion(region_dock1_no_chat)
            pos = state_machine.confirm_region('currentregion.png', './picture/ship_idle.png', 0.17, region_dock1_no_chat )
            if (pos):
                log.debug_msg("schiff angekommen")
                next_state = "center_ship"
            else:
                log.debug_msg("schiff unterwegs")

        case "center_ship":
            move_mouse(pos_dock1_no_chat)
            sleep(0.5)
            move_mouse(pos_location_btn_no_chat)
            next_state = "check_cargo"

        case "check_cargo":
            if num_of_targets != 0:
                if num_of_targets == target_count:
                    next_state = "send_home"
                else:
                    next_state = "find_target"
            else:
                pos = state_machine.confirm_region('currentregion.png', './picture/cargo_full.png', 0.17,
                                                   region_dock1_no_chat)
                if pos:
                    next_state = "send_home"
                else:
                    next_state = "find_target"

        case "find_target":
            if not enable_battle_screen:
                move_mouse_click(pos_battle_screen_btn)
                enable_battle_screen = 1
            if state_machine.attack_target(target_class):
                #1 battleship
                #2 int
                #3 science
                #4 miner
                target_count = target_count + 1
                log.debug_msg("Angriff Target " + str(target_count), 1)
            next_state = "wait_for_arrive"

        case "send_home":
            if enable_battle_screen:
                move_mouse_click(pos_battle_screen_btn)
                enable_battle_screen = 0
            move_mouse(pos_dock1_no_chat)
            sleep(0.5)
            move_mouse_click(pos_recall_btn_no_chat)
            next_state = "wait_until_home"

        case "wait_until_home":
            next_state = "none"
            pos = state_machine.confirm_region('currentregion.png', './picture/ship_in_station.png', 0.17, region_dock1_no_chat)
            if pos:
                print("passiert nicht")
            else:
                pos = state_machine.confirm_region('currentregion.png', './picture/ship_need_repair.png', 0.17,
                                                   region_dock1_no_chat)
                if pos:
                    #repair
                    move_mouse(pos_dock1_no_chat)
                    sleep(0.5)
                    #call for help
                    move_mouse_click(pos_recall_btn_no_chat)
                    sleep(0.5)
                    #spped up
                    move_mouse_click(pos_recall_btn_no_chat)
                    while not state_machine.confirm_screen('currentscreen.png', './picture/gratis_repair.png', 0.17):
                        move_mouse_click(pos_repair_screen_btn)
                        sleep(0.5)

        case "repair":
            print("interesant")
        case _:
            log.debug_msg("default_state")
    sleep(2)


loop_time = time()


debug_msg('Done.')