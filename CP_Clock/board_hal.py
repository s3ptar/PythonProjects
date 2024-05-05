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
import bitbangio
"""#####################################################################
# Informations
#####################################################################"""
#https://github.com/waveshareteam/e-Paper/blob/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd2in9b_V3.py
#https://github.com/mcauser/micropython-waveshare-epaper
#https://github.com/waveshareteam/e-Paper/blob/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd2in9b_V3.py
#https://github.com/waveshareteam/e-Paper/blob/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epdconfig.py#L116
#https://docs.circuitpython.org/en/latest/shared-bindings/bitbangio/index.html#bitbangio.SPI.__enter__
#https://github.com/mcauser/micropython-waveshare-epaper/blob/master/epaper2in9b.py
"""#####################################################################
# Declarations
#####################################################################"""

#print(dir(board))
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#EPD_SCK_PIN  = digitalio.DigitalInOut(board.D13)
#EPD_SCK_PIN.direction = digitalio.Direction.OUTPUT
#EPD_MOSI_PIN  = digitalio.DigitalInOut(board.D14)
#EPD_MOSI_PIN.direction = digitalio.Direction.OUTPUT
EPD_CS_PIN  = digitalio.DigitalInOut(board.D15)
EPD_CS_PIN.direction = digitalio.Direction.OUTPUT
EPD_RST_PIN  = digitalio.DigitalInOut(board.D26)
EPD_RST_PIN.direction = digitalio.Direction.OUTPUT
EPD_DC_PIN  = digitalio.DigitalInOut(board.D27)
EPD_DC_PIN.direction = digitalio.Direction.OUTPUT
EPD_BUSY_PIN  = digitalio.DigitalInOut(board.D25)
EPD_BUSY_PIN.direction = digitalio.Direction.INPUT
EDP_SPI = bitbangio.SPI(board.D13, board.D14)

#define EPD_SCK_PIN 13
#define EPD_MOSI_PIN 14
#define EPD_CS_PIN   15
#define EPD_RST_PIN  26
#define EPD_DC_PIN   27
#define EPD_BUSY_PIN 25

GPIO_PIN_SET =   1
GPIO_PIN_RESET = 0



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
#! \fn          def board_init():
#  \brief       board start function
#  \param       none
#  \exception   none
#  \return      none
#####################################################################"""
def board_init():
    #EPD_CS_PIN.value = True
    #EPD_CS_PIN.value =  GPIO_PIN_SET
    set_pin_value(EPD_CS_PIN, GPIO_PIN_SET)
    #EPD_SCK_PIN.value = False
    #EPD_SCK_PIN.value = GPIO_PIN_RESET
    set_pin_value(led, 0)
    

def led_on_off(on_off):
    led.value = on_off

"""#####################################################################
#! \fn          def set_pin_value(pin, state):
#  \brief       setup pin function
#  \param       pin - pin object
#  \param       state - pin state
#  \exception   none
#  \return      none
#####################################################################"""
def set_pin_value(pin, state):
    pin.value = state
    

