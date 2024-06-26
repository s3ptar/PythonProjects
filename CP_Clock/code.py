"""#####################################################################
#! \file:                   main.cpp
#  \projekt:                USB_HID
#  \created on:             2023 09 01
#  \author:                 R. Gräber
#  \version:                0
#  \history:                -
#  \brief
#####################################################################"""


"""#####################################################################
# Includes
#####################################################################"""
import time
import board
import digitalio
import board_hal
"""#####################################################################
# Informations
#####################################################################"""
#https://github.com/waveshareteam/e-Paper/blob/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd2in9b_V3.py
#https://github.com/mcauser/micropython-waveshare-epaper
"""#####################################################################
# Declarations
#####################################################################"""

"""#####################################################################
# Constant
#####################################################################"""


"""#####################################################################
# Global Variable
#####################################################################"""


"""#####################################################################
# local Variable
#####################################################################"""


"""#####################################################################
# Constant
#####################################################################"""

"""#####################################################################
# Local Funtions
#####################################################################"""






"""#####################################################################
#! \fn          int main(){
#  \brief       start up function
#  \param       none
#  \exception   none
#  \return      none
#####################################################################"""

if __name__ == "__main__":
    print("Hello World!")
    board_hal.board_init()
    #e = epaper2in9.EPD(spi, cs, dc, rst, busy)
    while True:
        #board_hal.led.value = 1
        board_hal.led_on_off(1)
        time.sleep(0.5)
        #board_hal.led.value = 0
        board_hal.led_on_off(0)
        time.sleep(0.5)