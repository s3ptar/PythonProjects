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

from pywinauto import keyboard
import json
from time import sleep
from pynput import keyboard
from pywinauto.keyboard import send_keys
#import keyboard
from threading import Thread
import threading
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
no_target_cnt = 0
start_time = time.time()
user_interaction = threading.Semaphore(1)

"""*********************************************************************
                mantis
*********************************************************************"""
json_config_data_mantis = """
    [
    {
    "target_system" : "yunke",
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":0,
        "miner":0
    }],
    "num_of_target_kills":999999,
    "num_of_repeats": 4,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""

json_config_data_swarm = """
    [
    {
    "target_system" : "beilum",
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":0,
        "miner":0
    }],
    "num_of_target_kills":75,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""

"""*********************************************************************
                dailys
                
*********************************************************************"""


json_config_data_ = """
    [
{
    "target_system" : "intello",
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":100,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""


json_config_data = """
    [
    {
    "target_system" : "Temminck",
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":25,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
},
{
    "target_system" : "axo'tae",
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":30,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
},
{
    "target_system" : "solis omega",
    "target_list":[{
        "battleship":1,
        "interceptor":0,
        "explorer":0,
        "miner":0
    }],
    "num_of_target_kills":30,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
},
{
    "target_system" : "lyrae nebula",
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":13,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
},
{
    "target_system" : "sivis", 
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":99999,
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""



json_config_data_sol = """
    [
    
{
    "target_system" : "sol",
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":0,
        "miner":1
    }],
    "num_of_target_kills":100,
    "num_of_repeats": 3,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""


"""*********************************************************************
                borg
*********************************************************************"""
json_config_data_ = """
    [{
    "target_system" : "solus ynestri", 
    "target_list":[{
        "battleship":1,
        "interceptor":0,
        "explorer":0,
        "miner":0
    }],
    "num_of_target_kills":999999,    
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""

"""*********************************************************************
                stella
*********************************************************************"""
json_config_data_f = """
    [{
    "target_system" : "lindstrom", 
    "target_list":[{
        "battleship":0,
        "interceptor":0,
        "explorer":0,
        "miner":1
    }],
    "num_of_target_kills":999999,    
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""

"""*********************************************************************
                beta sector  
*********************************************************************"""
json_config_data_beta = """
    [{
    "target_system" : "beta-sektor", 
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":50,
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""

"""*********************************************************************
                4 stat schiff parts
*********************************************************************"""
json_config_data_4 = """
    [{
    "target_system" : "sivis", 
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":99999,
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""

json_config_data_faction = """
    [
    {
    "target_system" : "intello",
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":40,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
},
{
    "target_system" : "mullins",
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":40,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
},
{
    "target_system" : "johbacor",
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":40,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""

json_config_data_ruhm = """
    [
    {
    "target_system" : "intello",
    "target_list":[{
    
    
    
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":999,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""


"""*********************************************************************
*! \fn          def on_press(key, abortKey='ctrl_l')
*  \brief       wait for user interrupt to pause the code
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def on_press(key, abortKey='ctrl_l'):
    user_interrupt = 1
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    #print('pressed %s' % (k))
    if k == abortKey:
        #print('end loop ...')
        if user_interaction._value:
            user_interaction.acquire()
        else:
            user_interaction.release()



def loop_fun():
    while True:
        if user_interaction._value:
            print('not sleeping')
        else:
            print('sleeping')

        sleep(5)




__name__ == '__main__'


#navigation.confirm_screen_grey("./picture/hostiles/interceptor.png", 0.4)


abortKey = 'ctrl_l'
listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
listener.start()  # start to listen on a separate thread
# start thread with loop
#Thread(target=loop_fun, args=(), name='loop_fun', daemon=True).start()
#listener.join() # wait for abortKey



# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("chat close")
navigation.close_chat_window()
print("repair")
#navigation.repair_ship(1)



print("start task")
task_data = json.loads(json_config_data)
for task_item in task_data:

    current_state = "send_to_system"
    next_state = "send_to_system"
    target_cnt = 0

    repeat_loops = task_item["num_of_repeats"]
    while repeat_loops:

        if not user_interaction._value:

            while not user_interaction._value:
                sleep(5)
                print("user pausing .. press ctrl links for ")


        sleep(2)
        current_state = next_state
        if current_state == "send_to_system":
            print("send to system " + task_item["target_system"])
            return_val = navigation.send_to_system(task_item["target_system"], 1)
            fighting_mode = 1
            if return_val:
                next_state = "wait_for_ship_arrive_system"
                threshold = 0.12

        if current_state == "wait_for_ship_arrive_system":
            return_val = navigation.wait_unilt_ship_rdy(1)
            if return_val:
                next_state = "attack_targets"
                #reset miss clicks
                no_target_cnt = 0
                threshold = 0.4


        if current_state == "attack_targets":
            #navigation.prepare_attacking()
            if navigation.attacking(task_item["target_list"], task_item["closed_kill_enable"]):
                target_cnt += 1
                next_state = "wait_for_ship_finish_attack"
                rt_time = (time.time() - start_time) / 60
                print("Killed Target : {kills} - runtime : {rt_time_min:3.0f}min".format(kills=target_cnt,
                                                                                         rt_time_min=rt_time))
            else:
                no_target_cnt += 1
                threshold = threshold + 0.02
                print(f'no target, threshold = {threshold}')
                if no_target_cnt > 5:
                    #zuviele fehlverscuhe, center ship
                    next_state = "send_to_system"


            """while fighting_mode:# or not task_item['cargo_modus_enabled']:
                #wait unitl ship arrive
                #navigation.prepare_attacking()
                if navigation.attacking(task_item["target_list"], task_item["closed_kill_enable"]):
                    target_cnt += 1
                    no_target_cnt = 0
                    rt_time = (time.time() - start_time)/60
                    print("Killed Target : {kills} - runtime : {rt_time_min:3.0f}min" .format(kills=target_cnt, rt_time_min=rt_time))
                    #print(f""Killed Target : {kills} - runtime : {rt_time_min} min"")
                else:
                    no_target_cnt += 1
                    # mehr als 5 fehlverscuhe nacheinander, shiff im system zerntrieren
                    if no_target_cnt > 5:
                        navigation.send_to_system(task_item["target_system"])
                        no_target_cnt = 0"""

        if current_state == "wait_for_ship_finish_attack":
            return_val = navigation.wait_unilt_ship_rdy(1)
            if return_val:
                if ((target_cnt >= task_item["num_of_target_kills"])):
                    #send ship home
                    send_keys('%m')
                    next_state = "send_ship_home"
                elif navigation.check_ship(1):
                    next_state = "send_ship_home"
                else:
                    next_state = "attack_targets"

        if current_state == "send_ship_home":
            return_val = navigation.wait_unilt_ship_rdy(1)
            if return_val:
                next_state = "repair_ship"
            sleep(4)

        if current_state == "repair_ship":
            return_val = navigation.repair_ship(1)
            if return_val:
                next_state = "send_to_system"
                repeat_loops -= 1








