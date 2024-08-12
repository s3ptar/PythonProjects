import json
import os
import navigation

"""*********************************************************************
*! \fn          main
*  \brief       start code
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""


import json

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
target_system = ["neara"]
#1 battleship
#2 int
#3 science
#4 miner
target_class = [1,1,1,1]
#target_class = [0,0,1,0]



json_config_data = """
    [{
    "target_system" : "corvinus",
    "target_list":[{
        "battleship":0,
        "interceptor":0,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":0
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
    print("send to system " + task_item["target_system"])
    #navigation.send_to_system(task_item["target_system"])
    while 1:
    #wait unitl ship arrive
        navigation.wait_unilt_ship_rdy(1)
        navigation.prepare_attacking()
        navigation.attacking(task_item["target_list"])


# initialize the Vision class


#wincap.saveRegion(region_dock1_no_chat)
#move_mouse_click((1200,540))
#sleep(200)


