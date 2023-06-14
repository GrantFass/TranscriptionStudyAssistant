/*********************************************************************************
 * Filename:      DeviceInterface.h
 * 
 * Description:   Device interface header file
 * 
 * Last Modified: 4/26/2023
 *********************************************************************************/ 
#ifndef DEVICE_INTERFACE
#define DEVICE_INTERFACE

#include <Stepper.h>
#include <esp32-hal-timer.h>

// Serial Constants
#define BAUD_RATE 115200
#define DEFAULT_TIMEOUT 5

// Motor Constants
#define STEPS 200
#define MOTOR_PIN1 25
#define MOTOR_PIN2 26
#define MOTOR_PIN3 27
#define MOTOR_PIN4 15

// Microphone Constants
#define MIC1 33
#define ALARM_CNT 227 // (1/44.1kHz)*(80000KHz/8) = 227 count (22.7us or 44.1KHz or 320Kbps)
#define TIMER0 0
#define PRESCALAR 8
#define MAX_SIZE 128

class DeviceInterface
{
public:
    // Initialization
    DeviceInterface(void);

    // Serial Functions
    // void open();
    // void close();

    // Motor Functions
    void setMotorSpeed(int speed);
    void moveMotor(int steps);

    // Microphone Functions
    void startAudioSampling(void);
    void stopAudioSampling(void);

private:
    // Intialize Stepper Motor
    Stepper motor = Stepper(STEPS, MOTOR_PIN1, MOTOR_PIN2, MOTOR_PIN3, MOTOR_PIN4);
    // Initialize Microphone Sampling Timer
    hw_timer_s* timer = timerBegin(TIMER0, PRESCALAR, true);
};

#endif /*DeviceInterface*/
