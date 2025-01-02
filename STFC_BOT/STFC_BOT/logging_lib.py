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

import inspect
import string

"""*********************************************************************
* Informations
*********************************************************************"""
# https://os.mbed.com/platforms/FRDM-K64F/#board-pinout
#https://stackoverflow.com/questions/13552907/way-to-pass-multiple-parameters-to-a-function-in-python
"""*********************************************************************
* Declarations
*********************************************************************"""

"""*********************************************************************
* Constant
*********************************************************************"""

logging_level_list = ["Error", "Warning", "Info", "Debug", "Verbose"]

"""*********************************************************************
* Global Variable
*********************************************************************"""
default_log_lvl = 2
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
*! \fn          int main(){
*  \brief       start up function
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
def logging_msg(*args, **kwargs):

    lvl_info = logging_level_list[default_log_lvl]
    log_msg = ""

    #check if available
    try:
        len(kwargs["lvl"])
    except:
        lvl_info = logging_level_list[default_log_lvl]
    else:
        lvl_info = kwargs["lvl"]

    call_fct = (inspect.stack()[1].filename).split('\\')[-1] + " -> " + inspect.stack()[1].function
    #check if string , than print
    if isinstance(kwargs["msg"],str):

        print(lvl_info + ", " + call_fct + ", " + kwargs["msg"])
