/*********************************************************************************
 * Filename:      DeviceInterface.h
 * 
 * Description:   Provides function for interfacing with the device's
 *                microphone and motor.
 * 
 * Last Modified: 5/14/2023
 *********************************************************************************/
#include "DeviceInterface.h"
#include <Arduino.h>

// Audio Buffer
static uint16_t audio_buff[MAX_SIZE] = {0};
static uint8_t idx = 0;

// Misc Variables
volatile bool audioTransmissionActive = false;

/**
 * sampleAudio: Audio sampling ISR. Reads a value from the ADC pin that the
 *              omnidirectional microphone is connected to. Store samples
 *              in the audio buffer.
 * 
 * Parameters: none
 * 
 * Return: None
*/
void IRAM_ATTR sampleAudio()
{
    // Continues to store samples into the audio buffer
    if (idx != MAX_SIZE)
    {
        audio_buff[idx] = analogRead(MIC1);
        ++idx;
    }
    else if (idx == MAX_SIZE)
    {
        // Reset buffer index
        idx = 0;

        if(audioTransmissionActive){
            Serial.println("AUDIO BIT " + String(MAX_SIZE));
            for(int i = 0; i < MAX_SIZE; i++){
                Serial.write(audio_buff[i]);
            }
        }
    }
}

/* Initialization */
DeviceInterface::DeviceInterface()
{
    /* Microphone Initialization */
    timerAttachInterrupt(timer, &sampleAudio, false);
    timerAlarmWrite(timer, ALARM_CNT, true);
}

/* Motor Functions */
/**
 * setMotorSpeed: Sets the motor speed to the given value.
 *                Assumes the motor has already been initialized.
 * 
 * Parameters:
 *  speed - speed of motor in RPMs
 * 
 * Return: none
*/
void DeviceInterface::setMotorSpeed(int speed)
{
    motor.setSpeed(speed);
}

/**
 * moveMotor: Moves the motor based on the given number of steps.
 *            A postive number of steps moves the motor forward.
 *            A negative number of steps moves the motor backwards.
 *            Assumes the motor has already been initialized.
 * 
 * Parameters:
 *  steps - number of steps to move the motor
 * 
 * Return: none
*/
void DeviceInterface::moveMotor(int steps)
{
    motor.step(steps);
}

/* Microphone Functions */
/**
 * startAudioSampling: Enables the audio sampling interrupt
 * 
 * Parameters: none
 * 
 * Return: none
*/
void DeviceInterface::startAudioSampling(void)
{
    // Reset the timer
    timerRestart(timer);
    // Start the timer if not running
    if(!timerStarted(timer))
    {
        timerStart(timer);
    }
    // Enable the alarm if not currently enabled
    if(!timerAlarmEnabled(timer))
    {
        timerAlarmEnable(timer);
    }
    audioTransmissionActive = true;
}

/**
 * stopAudioSampling: Disables the audio sampling interrupt
 * 
 * Parameters: none
 * 
 * Return: none
*/
void DeviceInterface::stopAudioSampling(void)
{
    // Disable the alarm if it's currently enabled
    if(timerAlarmEnabled(timer))
    {
        timerAlarmDisable(timer);
    }
    // Stop the timer if currently running
    if(timerStarted(timer))
    {
        timerStop(timer);
    }
    audioTransmissionActive = false;
}
