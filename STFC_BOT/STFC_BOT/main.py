import json
import os
import navigation
import datetime
from datetime import timedelta
import time
"""*********************************************************************
*! \fn          main
*  \brief       start code
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""


import json
from time import sleep

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

start_time = time.time()

json_config_data = """
    [{
    "target_system" : "beta-sektor",
    "target_list":[{
        "battleship":1,
        "interceptor":2,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":0,
    "num_of_repeats": 2,
    "cargo_modus_enabled":0
}]
"""
"""*********************************************************************
*! \fn          move_mouse(target_pos)
*  \brief       set mouse to posotion and click
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""


__name__ == '__main__'

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("chat close")
#navigation.close_chat_window()
print("repair")
#navigation.repair_ship()

print("start task")
task_data = json.loads(json_config_data)
for task_item in task_data:

    repeat_loops = task_item["num_of_repeats"]
    while repeat_loops:

        print("send to system " + task_item["target_system"])
        navigation.send_to_system(task_item["target_system"])
        target_cnt = 0
        fighting_mode = 1

        navigation.wait_unilt_ship_rdy(1)
        navigation.prepare_attacking()
        while fighting_mode:# or not task_item['cargo_modus_enabled']:
            #wait unitl ship arrive
            navigation.prepare_attacking()
            if navigation.attacking(task_item["target_list"]):
                target_cnt += 1
                rt_time = (time.time() - start_time)/60
                print("Killed Target : {kills} - runtime : {rt_time_min:3.0f}min" .format(kills=target_cnt, rt_time_min=rt_time))
                #print(f""Killed Target : {kills} - runtime : {rt_time_min} min"")

            navigation.wait_unilt_ship_rdy(1)
            fighting_mode = navigation.check_ship(1)


        sleep(4)
        #send home
        navigation.check_ship(1)
        navigation.wait_unilt_ship_rdy(1)
        navigation.repair_ship(1)
        repeat_loops -= 1



