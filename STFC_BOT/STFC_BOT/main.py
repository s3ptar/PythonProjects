import json
import os
import navigation
import attacking
import datetime
from datetime import timedelta
import time
import sys

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
# import keyboard
from threading import Thread
import threading
import logging_lib

"""*********************************************************************
                Constant
*********************************************************************"""
# without chat
pos_dock1_no_chat = (750, 950)
region_dock1_no_chat = (650, 910, 90, 110)
pos_attack_btn_no_chat = (1300, 600)
pos_location_btn_no_chat = (100, 910)
pos_recall_btn_no_chat = (100, 980)
pos_close_chat_btn = (500, 20)
pos_repair_screen_btn = (1200, 540)
pos_battle_screen_btn = (1860, 850)



dummy = 0

"""*********************************************************************
                local val
*********************************************************************"""


user_interaction = threading.Semaphore(1)
"""*********************************************************************
                mantis
*********************************************************************"""
json_config_data_mantis = """
    [
    {
    "target_system" : "yunke",
    "timeout_fly_to_sys" : 60,
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":0,
        "miner":0
    }],
    "num_of_target_kills":50,
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
    "timeout_fly_to_sys" : 60,
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":0,
        "miner":0
    }],
    "num_of_target_kills":75,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""


"""*********************************************************************
                dailys

*********************************************************************"""


json_config_data_4g = """
    [
{
    "target_system" : "sivis", 
    "timeout_fly_to_sys" : 120,
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":52,
    "num_of_repeats": 4,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""

json_config_data_sipra = """
    [
{
    "target_system" : "sirpa", 
    "timeout_fly_to_sys" : 60,
    "target_list":[{
        "battleship":1,
        "interceptor":0,
        "explorer":0,
        "miner":1
    }],
    "num_of_target_kills":100,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""



json_config_data = """
    [
{
    "target_system" : "Solis Omega",
    "timeout_fly_to_sys" : 300,
    "target_list":[{
        "battleship":1,
        "interceptor":0,
        "explorer":0,
        "miner":0
    }],
    "num_of_target_kills":100,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
},
{
    "target_system" : "axo'tae",
    "timeout_fly_to_sys" : 60,
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":20,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
},
{
    "target_system" : "mehruunahd", 
    "timeout_fly_to_sys" : 120,
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":18,
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
},
   {
    "target_system" : "Cirriped",
    "timeout_fly_to_sys" : 90,
    "target_list":[{
        "battleship":1,
        "interceptor":0,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":25,
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""
json_config_data_egal = """
    [
{
    "target_system" : "Mirror Dhi'Ban",
    "timeout_fly_to_sys" : 10,
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":1
    }],
    "num_of_target_kills":200,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""

json_config_data_4g_vessel = """
    [

{
    "target_system" : "sol",
    "timeout_fly_to_sys" : 60,
    "target_list":[{
        "battleship":0,
        "interceptor":1,
        "explorer":0,
        "miner":1
    }],
    "num_of_target_kills":75,
    "num_of_repeats": 4,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""

"""*********************************************************************
                borg
*********************************************************************"""
json_config_data_borg = """
    [{
    "target_system" : "jovia", 
    "timeout_fly_to_sys" : 60,
    "target_list":[{
        "battleship":1,
        "interceptor":0,
        "explorer":0,
        "miner":0
    }],
    "num_of_target_kills":999999,    
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""

"""*********************************************************************
                stella
*********************************************************************"""
json_config_data_f = """
    [{
    "target_system" : "lindstrom", 
    "timeout_fly_to_sys" : 60,
    "target_list":[{
        "battleship":0,
        "interceptor":0,
        "explorer":0,
        "miner":1
    }],
    "num_of_target_kills":999999,    
    "num_of_repeats": 2,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""

"""*********************************************************************
                beta sector  - data pads
*********************************************************************"""
json_config_load = """
    [{
    "target_system" : "beta-sektor", 
    "timeout_fly_to_sys" : 90,
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":100,
    "num_of_repeats": 4,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""


"""*********************************************************************
                fatu
*********************************************************************"""
json_config_data_fatu = """
    [{
    "target_system" : "litzarr", 
    "timeout_fly_to_sys" : 120,
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":200,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":0
}
]
"""

json_config_data_fac = """
    [

{
    "target_system" : "mullins",
    "timeout_fly_to_sys" : 300,
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":75,
    "num_of_repeats": 5,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
},
{
    "target_system" : "johbacor",
    "timeout_fly_to_sys" : 300,
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":60,
    "num_of_repeats": 1,
    "closed_kill_enable":1,
    "cargo_modus_enabled":1
}
]
"""


#gorn
json_config_data_gorn = """
    [
    {
    "target_system" : "dendroa",
    "timeout_fly_to_sys" : 90,
    "target_list":[{
        "battleship":1,
        "interceptor":1,
        "explorer":1,
        "miner":0
    }],
    "num_of_target_kills":40,
    "num_of_repeats": 3,
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

    # print('pressed %s' % (k))
    if k == abortKey:
        # print('end loop ...')
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

"""*********************************************************************
*! \fn          worker(sum_of_loops=None, json_config_data)
*  \brief       work functon, loop through the tasks
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def worker(json_config_data=None):
    current_state = "init"
    next_state = "init"
    prev_state = "init"
    target_count = 0
    enable_battle_screen = 0
    no_target_cnt = 0
    retry_target_cnt = 0
    start_time = time.time()
    bl_rist_time_rep = 0
    var_step_error_cnt = 0
    sum_of_loops = 0
    loops = 1
    var_time_out_to_systems_sec = 0

    if json_config_data == None:
        exit()

    print("start task")
    task_data = json.loads(json_config_data)

    for item in task_data:
        mycnt = item['num_of_repeats']
        sum_of_loops += mycnt

    for task_item in task_data:

        current_state = "send_to_system"
        next_state = "send_to_system"
        target_cnt = 0
        var_time_out_to_systems_sec = task_item["timeout_fly_to_sys"]

        repeat_loops = task_item["num_of_repeats"]
        while repeat_loops:

            if not user_interaction._value:
                while not user_interaction._value:
                    sleep(10)
                    print("user pausing .. press ctrl links for ")

            sleep(1)
            #detect next states
            prev_state = current_state
            current_state = next_state

            # no change
            if prev_state == current_state:
                var_step_error_cnt=var_step_error_cnt + 1
                #print("Looperror : {no_of_error}".format(no_of_error=var_step_error_cnt))
            else:
                var_step_error_cnt=0

            if var_step_error_cnt > 30:
                var_step_error_cnt=0
                navigation.restart_game()

            rt_time = (time.time() - start_time) / 60
            if rt_time >= 500:
                navigation.close_game()
                sys.exit("Stop after 400min")

            #print status
            print("Status Report: State : {task_current_state}, System : {activ_system}, StepError : {error_progr}, "
                  "target: {trg_cnt} / todo : {trg_to_do}, Run : {loop_cnt} : Runs {all_repeats},  "
                  "runtime : {rt_time_min:3.0f}min".format(
                    error_progr=var_step_error_cnt,
                    task_current_state=current_state,
                    activ_system=task_item["target_system"],
                    trg_cnt=target_cnt,
                    trg_to_do=task_item["num_of_target_kills"],
                    loop_cnt=loops,
                    all_repeats=sum_of_loops,
                    rt_time_min=rt_time))
            # print("Killed Target : {kills} / {kills_to_go} - runtime : {rt_time_min:3.0f}min".format(
            #    kills=target_cnt, kills_to_go=task_item["num_of_target_kills"], rt_time_min=rt_time))



            """
            Start sending ship out in space
            """
            if current_state == "send_to_system":
                #print("send to system " + task_item["target_system"])
                return_val = navigation.send_to_system(task_item["target_system"], 1)
                fighting_mode = 1
                if return_val:
                    next_state = "wait_for_ship_arrive_system"
                    threshold = 0.12
                    threshold = 0.20
                    #wait for start
                    sleep(10)

            if current_state == "wait_for_ship_arrive_system":
                sleep(var_time_out_to_systems_sec)
                return_val = navigation.wait_unilt_ship_rdy(1)
                if return_val > 0 & return_val < 99:
                    next_state = "attack_targets"
                    var_time_out_to_systems_sec = 20
                    # reset miss clicks
                    no_target_cnt = 0
                    threshold = 0.4
                if return_val == 99:
                    next_state = "send_to_system"

            if current_state == "attack_targets":
                # navigation.prepare_attacking()
                if attacking.attacking(task_item["target_list"], task_item["closed_kill_enable"]):
                    target_cnt += 1
                    retry_target_cnt += 1
                    retry_target_cnt = 0
                    no_target_cnt = 0
                    next_state = "wait_for_ship_finish_attack"
                    rt_time = (time.time() - start_time) / 60
                    #print("Killed Target : {kills} / {kills_to_go} - runtime : {rt_time_min:3.0f}min".format(
                    #    kills=target_cnt, kills_to_go=task_item["num_of_target_kills"], rt_time_min=rt_time))

                else:
                    no_target_cnt += 1
                    # no_target_cnt = 0
                    threshold = threshold + 0.02

                    #print(f'no target, threshold = {threshold}')

                    if retry_target_cnt > 10:
                        retry_target_cnt = 0
                        navigation.check_miss_clicks()

                    if no_target_cnt > 5:
                        # zuviele fehlverscuhe, center ship
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
                        # send ship home
                        sleep(2)
                        send_keys('%m')
                        send_keys('%m')
                        send_keys('%m')
                        next_state = "send_ship_home"
                    elif navigation.check_ship(1, task_item["cargo_modus_enabled"]):
                        next_state = "send_ship_home"
                    else:
                        next_state = "attack_targets"

            if current_state == "send_ship_home":
                sleep(task_item["timeout_fly_to_sys"])
                return_val = navigation.wait_unilt_ship_rdy(1)
                if return_val:
                    next_state = "repair_ship"
                else:
                    sleep(2)
                    send_keys('%m')
                    send_keys('%m')
                    send_keys('%m')
                sleep(4)

            if current_state == "repair_ship":
                target_cnt = 0
                return_val = navigation.repair_ship(1, bl_rist_time_rep)
                bl_rist_time_rep = 1
                if return_val:
                    next_state = "send_to_system"
                    var_time_out_to_systems_sec = task_item["timeout_fly_to_sys"]
                    repeat_loops -= 1
                    loops = loops + 1
                    bl_rist_time_rep = 0
    navigation.close_game()


if __name__ == "__main__":

    #try close and reboot
    #navigation.restart_game()
    #navigation.repair_ship(1,1)


    abortKey = 'ctrl_l'
    listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
    listener.start()  # start to listen on a separate thread
    # start thread with loop
    # Thread(target=loop_fun, args=(), name='loop_fun', daemon=True).start()
    # listener.join() # wait for abortKey
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    #attacking.test_log()
    #logging_lib.logging_msg(msg="test")

    print("chat close")
    navigation.close_chat_window()
    print("repair")
    # navigation.repair_ship(1)
    worker(json_config_load)
