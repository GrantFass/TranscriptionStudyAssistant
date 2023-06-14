/************************************************************************
 * Filename: Main.ino
 * 
 * Description: Initializes the device and runs function calls received
 *              over the the USB connection to the user's laptop.
 * 
 * Last Modified: 5/14/2023
*************************************************************************/

// Dependencies
#include "DeviceInterface.h"
#include <stdlib.h>

// Directives
using namespace std;

// Config Values
String COMMAND_DELIMITER = " ";

// Initialize Device Interface
DeviceInterface DeviceInterface;

// Misc Variables
String serial;

// Initialize the Device
void setup()
{
    // General setup
    Serial.begin(BAUD_RATE);
    Serial.setTimeout(DEFAULT_TIMEOUT);
    
    // Motor Setup
    DeviceInterface.setMotorSpeed(80);
}

// Listen for function calls, then execute them
void loop()
{
    /* Motor Function Test*/
    // DeviceInterface.moveMotor(60);
    // delay(1000);
    // DeviceInterface.moveMotor(-60);
    // delay(1000);

    /* Microphone Function Test*/
    // Serial.println("Start");
    // DeviceInterface.startAudioSampling();
    // delay(1000);
    // Serial.println("Stop");
    // DeviceInterface.stopAudioSampling();
    // delay(1000);

    /* Main Code */
    while(Serial.available() == 0){
        
    }
    serial = Serial.readString();
    serial.trim();
    serial.toUpperCase();

    // Tokenize
    String category;
    String directive;
    String data = "";

    int start, end = -1*COMMAND_DELIMITER.length();
    int i = 0;
    do{
        start = end + COMMAND_DELIMITER.length();
        end = serial.indexOf(COMMAND_DELIMITER, start);

        String datum = serial.substring(start, end);

        if(i == 0){ // Category
        category = datum;
        }
        else if(i == 1){
        directive = datum;
        }
        else{
        data += " " + datum;
        }

        i++;
    } while (end != -1);

    if(category == "MOTOR"){ // Motor Stuff
        if(directive == "SPEED"){
        int speed = data.toInt();
        // Serial.println("Setting motor to speed " + String(speed));
        DeviceInterface.setMotorSpeed(speed);
        }
        else if(directive == "STEP"){
        int steps = data.toInt();
        // Serial.println("Moving motor " + String(steps) + " steps");
        DeviceInterface.moveMotor(steps);
        }
    }
    else if(category == "AUDIO"){
        Serial.println("Audio");
        if(directive == "START"){
        DeviceInterface.startAudioSampling();
        }
        else if(directive == "STOP"){
        DeviceInterface.stopAudioSampling();
        }
    }
    else if(category == "PING"){
        Serial.println("pong");
    }
}
