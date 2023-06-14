import serial
from serial import Serial
from serial.tools import list_ports
import time
from interface import Device

def callback(data:bytes) -> None:
    print(data)
    
with Device("COM7") as device:
    input("Press any key to start.")

    ## Example: Set motor to move
    # device.motorSpeed(80)
    # device.motorStep(30)

    ## Example: Print raw audio feed
    # device.startAudioFeed(callback)

    ## Example: Ping-Pong
    # print(device.ping())