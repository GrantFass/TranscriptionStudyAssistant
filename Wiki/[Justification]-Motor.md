[[_TOC_]]

## Potential Technology Options
A motor may be used to adjust the camera or microphone direction. There are several types that need to be investigated.  

The two types of motors that will probably work best for this application are brushless motors and stepper motors. A brushless motor would be quieter, which is important if near a microphone. A stepper motor may not be as quiet as a brushless motor, but it will offer the precision that we are looking for in this application.  
  
Why not the others?  
- Both the brushed motor and servo motor will not offer the quiet sound that we are looking for in this product.
- Both motors also don't provide the precision that we need.
- Brushed motors and servo motors are better for higher speed applications, which is not needed for this project.
- Servo motors may twitch while attempting to hold its position, which is not something we would want if attached to a camera.  

_**Examples**_  
| Name | Type | Price (per unit) | Link |  
| ------ | ------ | ------ | -------|  
| FIT0441 | Brushless Motor | $19.90 | https://www.digikey.com/en/products/detail/dfrobot/FIT0441/6588579?utm_adgroup=Motors%20-%20AC%2C%20DC&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Motors%2C%20Solenoids%2C%20Driver%20Boards%2FModules_NEW&utm_term=&utm_content=Motors%20-%20AC%2C%20DC&gclid=CjwKCAjwqJSaBhBUEiwAg5W9p7EXaeKc2d3jhUgX1qwoeMx0vyBFBr2136JFLad9uqhLWdL3pFWLMhoChE0QAvD_BwE |  
| QMOT QSH4218 | Stepper Motor | $50.76 | https://www.mouser.com/ProductDetail/Trinamic/QSH4218-35-10-027?qs=sGAEpiMZZMtt6tuQNKDHLCYkKjDAWuAUR5ijUav0AkU%3D |
| QMOT QSH5718 | Stepper Motor | $62.23 | https://www.mouser.com/ProductDetail/Trinamic/QSH5718-56-28-126?qs=sGAEpiMZZMtt6tuQNKDHLCYkKjDAWuAU5MS0KE7wH%252BQ%3D |

Note that NEMA-23 motors are a bit big. May want something closer to a NEMA-8

## Evaluation Strategies
What needs to be taken into consideration:  
- Speed
- Precision
- Noise Level

_**Speed**_  
For this application, we don't need a high speed device since a camera or microphone will work best is positioned slowly.  

_**Precision**_  
We would want as precise of a device as possible. It's important to make sure that a camera or microphone could be set to its intended position with a low amount of error.  

_**Noise Level**_  
If we design a custom device, we are going to have a microphone nearby the motor, so the noise level needs to be low to prevent the microphone from picking this up. The goal is to avoid distorting the audio as much as possible.  

_**Type of Devices**_  
The devices we can choose from include a _brushed DC motor_, a _brushless DC motor_, a _stepper motor_, and a _servo motor_.  

_**Additional Notes**_  
If we decide to design a custom device, further research will need to be done on a motor driver board since this will be needed to control the motor. This research can be deferred though until a decision has been made.  

_**References**_  
https://www.seeedstudio.com/blog/2019/04/01/choosing-the-right-motor-for-your-project-dc-vs-stepper-vs-servo-motors/ 

## Choice & Rationale

### Selection
[Mini Stepper Motor - 200 Steps - 20x30mm NEMA-8 Size](https://www.adafruit.com/product/4411#technical-details)  

Supporting Hardware:  
[Adafruit DRV8833 DC/Stepper Motor Driver Breakout Board](https://www.adafruit.com/product/3297?gclid=Cj0KCQiAmaibBhCAARIsAKUlaKSYO4Ty2oJ394hDtBIB1ueerKhA6fh2JX1YMjKW4mWmnOQhx8DP-hUaAtkkEALw_wcB)

### Reasoning
#### Why a Stepper Motor?
The devices we can choose from include a *brushed DC motor*, a *brushless DC motor*, a *stepper motor*, and a *servo motor*.

For this project, we will primarily be using the motor for accurately positioning the camera. Because this is our main focus, we will need a motor that will be precise. The motor will also be placed close to the microphone in our device, so it needs to be relatively quiet to prevent from interfering with the lecture audio. The motor can be slower since speed is not a main concern for this particular application.

A _stepper motor_ is the better fit for our product. This type of motor offers the precision that we are looking for without the need for an encoder. The motor can be operated by using a pulse generator.  

While a _stepper motor_ may not be as quiet as a _brushless DC motor_, we can work around the motor noise issues. Position accuracy is more important because camera placement issues will interfere with our video data more severely than motor noise will with the audio data. It's more difficult to recover from bad camera placement or incorrect camera following of a presenter than it is from some noise interference.  

As for _brushed DC motors_ and _servo motors_, they will be louder and will not provide the precision that we need. _Brushed motors_ and _servo motors_ are better for higher speed applications, which is not needed for this project. In addition to this, servo motors may twitch while attempting to hold its position, which is not something we would want if attached to a camera.

#### Why the Mini Stepper Motor - 200 Steps - 20x30mm NEMA-8 Size?
The examples outlined in the [Technology Report](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/Technology%20Report#motor-options) are all too large for this product. We need a smaller sized motor, which is why the examples outlined in issue #58 are all NEMA 8 stepper motors. The mini stepper motor from Adafruit has similar characteristics to the other outlined examples from issue #58. One of the bigger differences is price. Choosing this motor will help keep the cost down of the final product, especially since we will also need a motor driver to operate the motor. For this device, we would need a motor that can run with low voltage and has a maximum current rating at around 500mA. The mini stepper motor from Adafruit fits with this criteria since it has a voltage rating of 3.9V and a maximum current rating of 600mA. A coil resistance of 7 Ohms will work for this particular application as well. Along with this, a step degree of 1.8 will provide us with the precision that we need.

#### Why the Adafruit DRV8833 DC/Stepper Motor Driver Breakout Board?
The main reason this driver was selected is that it can drive stepper motors that run at lower voltage levels. The motor that we have selected has a voltage rating of 3.9V. The Adafruit DRV8833 motor driver board can operate with from 2.7V to 10.8V motor power. This motor driver can only drive one stepper motor. We are only using one stepper motor, so this fits with our device. Along with this, it provides current limiting capabilities to prevent from overdriving. It is also a small size, so it will fit within our device. Some soldering is required with this board, but there are members of the team that have soldering experience so this will not be an issue.

### Possible Challenges 
- The noise from the motor may interfere with the lecture audio
  - Once we go through the prototyping phase, we may find that the motor noise may not be that distracting
  - We could also dampen the noise by putting material around the motor to prevent the microphone from picking it up
- The drive shaft doesn't have a flat side, so friction clamping will need to be used to attach anything to the motor. We may end up damaging the motor in the process.
  - We could prevent this by researching how to do this without causing damage to the motor
  - We could also ask professors and other students for tips on how to do this without causing any significant damage to the motor
  - The vendor claims that the motor can be clamped pretty easily, so this may not be the biggest issue
- We have to make sure that the motor doesn't end up overheating while in use, which is something we will find out when we begin testing our prototype

## Prototypes & Images
See #142











