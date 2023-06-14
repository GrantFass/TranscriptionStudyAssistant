#####################################################################
## Project: Senior Design - interface
## Author: Xander Karpov
## Date: 2 May. 2023
## Provides: Interface library for sending information to the study
##	assist device.
#####################################################################

## Dependencies
from serial import Serial
from serial.tools.list_ports_common import ListPortInfo
from serial.tools import list_ports
from typing import List, Callable, Literal, Union
from typing_extensions import Self
from time import sleep
from threading import Thread, Event

## Config Values
BAUDRATE = 115200
TIMEOUT = 0.1

## Misc Values


## Public Functions
def listPortInfo() -> List[ListPortInfo]:
    """ Lists the currently available COM ports on the host PC.

    Returns
    --------
    List[ListPortInfo]
        List of ports information.
    """
    return list(list_ports.comports())

## Public Classes
class Device:
    """Class designed to abstract away the device."""
#region Private Methods
    #region Serial
    def __send(self, data:bytes) -> None:
        """ Sends commands in the raw form to the device via serial.
        
        Params
        --------
        data : bytes
            Byte data to send to the device.
        """
        self.__object.write(data)

    def __recv(self) -> bytes:
        """ Receives data from the device.
        Received data must end in a newline '\n' character.
        
        Returns
        --------
        bytes
            Bytes object containing the received data.
        """

        return self.__object.readline()

    def __sendStr(self, data:str) -> None:
        """ Sends a string to the device via serial.
        
        Params
        --------
        data : str
            String data to send.
        """
        self.__send(str(data).encode())

    def __recvStr(self) -> str:
        """ Receives string data from the device.
        Received data must end in a newline '\n' character.

        Returns
        --------
        str
            Received string data.
        """
        return self.__recv().decode("unicode_escape").strip()
    
    def __query(self, data:bytes) -> bytes:
        """ Sends byte data to the device and waits for its response.
        Response must end in a newline '\n' character.

        Params
        --------
        data : bytes
            Byte data to send to device.

        Returns
        --------
        bytes
            Received byte data.
        """
        self.__send(data)
        return self.__recv()
    
    def __queryStr(self, data:str) -> str:
        """ Sends string data to the device and waits for its response.
        Response must end in a newline '\n' character.

        Params
        --------
        data : str
            String data to send to the device.

        Returns
        --------
        str
            Received string data.
        """
        self.__sendStr(data)
        return self.__recvStr()
    #endregion Serial
    
    def __handleAudioFeed(self, callback:Callable[[bytes], None]) -> None:
        """ Private function to handle received audio samples.
        
        Params
        --------
        callback : (bytes) -> None
            Callback function which will be passed the data once it is received.
        """
        while not self.__flag_stopAudioFeed.is_set():
            got = self.__recvStr().upper()
            gotargs = got.split(" ")

            if len(gotargs) == 3:
                if gotargs[0] == "AUDIO" and gotargs[1] == "BIT":
                    numBytes = int(gotargs[2])
                    buffer = []
                    for _ in range(numBytes):
                        buffer.append(
                            self.__object.read()
                        )

                    callback(
                        (b"").join(buffer)
                    )
#endregion Private Methods

#region Constructor
    def __init__(self, port:str) -> None:
        """ Constructor.
        
        Params
        --------
        port : str
            Device's COM port. i.e. "COM7"
        """
        self.__port:str = port

        self.__audioFeed = None

        self.__flag_stopAudioFeed = Event()

        self.__object:Serial = None
#endregion Constructor

#region Public Methods
    #region Raw Commands
    def rawRead(self) -> str:
        """ Bypass function to call `self.__recvStr`.
        
        Returns
        --------
        str
            Results of `self.__recvStr()`.
        """
        return self.__recvStr()
    #endregion Raw Commands

    #region Connectivity Commands
    def ping(self) -> Union[Literal[""], Literal["pong"]]:
        """ Pings the device.
        This will return 'pong' once the device is good to talk.
        
        Returns
        --------
        Union[Literal[""], Literal["pong"]]
            Return message.
        """
        return self.__queryStr("ping")
    #endregion Connectivity Commands

    #region Motor Control
    def motorSpeed(self, speed:int) -> None:
        """ Sets the motor speed of the stepper motor.
        NOTE: This sets the speed of the stepper motor, but does not
            actually move it. Use `motorStep` to move the motor.

        Params
        --------
        speed : int
            Speed of the stepper motor.
        """
        self.__sendStr(f"motor speed {speed}")

    def motorStep(self, steps:int) -> None:
        """ Directs the stepper motor to move `steps` amount of steps.

        According to motor config, it has 200 steps, so that's about
            1.8 degrees per step, assuming half-stepping isn't a thing.

        Params
        --------
        steps : int
            Amount of steps to take (positive or negative).
        """
        self.__sendStr(f"motor step {steps}")
        
    #endregion Motor Control

    #region Microphone Control
    def startAudioFeed(self, callback:Callable[[bytes], None]) -> None:
        """ Directs the device to start the audio feed.
        Said audio feed will then be piped into the passed in callback,
            which will be executed in its own thread.
        
        Params
        --------
        callback : (bytes) -> None
            Callback which will handle the audio processing.
        """
        
        # Clear flag
        self.__flag_stopAudioFeed.clear()

        # Setup thread to handle reads and pass to callback
        self.__audioFeed = Thread(target=self.__handleAudioFeed, args=[callback])

        # Go
        self.__sendStr("AuDIO START")
        self.__audioFeed.start()

    def stopAudioFeed(self) -> None:
        """ Directs the device to stop the audio feed.
        This will also kill off the callback function at earliest
            convenience.
        """
        self.__flag_stopAudioFeed.set()
        self.__sendStr("AUDIO STOP")
    #endregion Microphone Control
    
    def open(self) -> None:
        """Opens the device."""
        global BAUDRATE
        global TIMEOUT

        self.__object = Serial(self.__port, baudrate=BAUDRATE, timeout=TIMEOUT)

        return self
    
    def close(self) -> None:
        """Closes the device."""
        self.__object.close()
#endregion Public Methods

#region Dunder Methods
    def __enter__(self) -> Self:
        """Allows class to be used with the `with` statement."""
        self.open()
        return self

    def __exit__(self, *_) -> None:
        """Allows class to be used with the `with` statement."""
        self.close()
#endregion Dunder Methods
    




## Go
if __name__ == "__main__":
    print(listPortInfo())