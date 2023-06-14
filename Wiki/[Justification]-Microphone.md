[[_TOC_]]

## Potential Technology Options

_Electret Condenser_ microphone may be the best because of the high sensitivity, which will be needed if the instructor's voice needs to be picked up from long distances
- Typical sensitivity range: 8 to 32 mV/Pa or -42 to -30 dB re 1V/Pa
- Will require less gain
- Cheaper than condenser mics
- Can work on lower battery supplies
	
Why not other types?
- _Ribbon microphones_ are better for studio recordings. While we do care about quality, we don't need studio quality for the purposes of picking up lecture audio
- _Dynamic microphones_ are better in louder settings because of their lower sensitivity. If we go with a device that sits out a desk, we would want a higher sensitivity microphone to pick up the instructor's audio from farther distances, so a dynamic microphone will not be best for this scenario.

_**Examples**_  
| Name   | Type   | Direction | Sensitivity (at 94dB SPL) | S/N Ratio | Frequency Range | Impedance | Price (per unit) | Link |
| ------ | ------ | --------- | ------------------------- | --------- | --------------- | --------- | ----- | ---- |
| CMC-9745-37T2 | Electret Condenser | Unidirectional | -37dB +- 3dB | 69dB | 100Hz-12kHz | 2kOhms | $3.33 | [CMC-9745-37T2](https://www.digikey.com/en/products/detail/cui-devices/CMC-9745-37T2/6561069)
| CMC-6035-130T | Electret Condenser | Omnidirectional | -42dB +- 3dB | 70dB | 100Hz-20kHz | 2.2kOhms | $2.57 | [CMC-6035-130T](https://www.digikey.com/en/products/detail/cui-devices/CMC-6035-130T/7784322) |
| BG-MIC-U1 | Electret Condenser | - | -53dB +- 3dB | - | 30Hz-12kHz | - | $190 | [BG-MIC-U1](https://www.digikey.com/en/products/detail/bzbgear/BG-MIC-U1/16532792) |  

These are just a few suggestions for now. Further research will need to be completed once a decision has been made about the direction we are going regarding the hardware design.
- These will most likely be used in our own device and are not suggestions of already existing microphone systems
- While more expensive, the BG-MIC-U1 seems to be close to a ready-to-go conference microphone.


## Evaluation Strategies

What needs to be taken into consideration:
- Sensitivity
- Maximum sound pressure level (SPL)
- Frequency Response
- Omnidirectional or Unidirectional
- Output Impedance

_**Sensitivity**_  
For a college-level classroom environment, we would want the microphone to pick up sound at a conversational level
- For this reason, we may be looking at picking up sounds at around 65dB
	
Higher Sensitivity Microphone
- good for picking up clearer sounds from a distance
- needs less gain to pick up clearer sounds
- may work better in a soundproof environment
	
Low Sensitivity Microphone
- can be used to single out a voice in a non-soundproof zone
- Ribbon-mic shouldn't be used in front of a large gust of air because this may cause the ribbon to stretch or snap
   - This would require a pop-guard or wind protection screen

_**Maximum SPL**_  
Higher quality microphones have a maximum SPL of around 164dB for condenser microphones
- This is for more expensive microphones so we will likely be below this level to prevent from having a high budget
	
_**Frequency Response**_  
Typical range 50Hz to 15kHz, so we will attempt to stay within this range.
	
_**Omnidirectional or Unidirectional**_  
An _omnidirectional microphone_ will pick up sound from all directions
- we may want to use this if we would like to get student input as well
- may be beneficial if the instructor is moving around the classroom and we don't have the microphone following the instructor
	
A _unidirectional microphone_ will pick up sounds located closer to the front of the microphone
- we may want to use this if we would like to single out the instructor's voice from other noise in the room
- we may need to implement a feature which follows the instructor
   - this feature may also be used to switch to following student voices if questions/answers/comments are spoken by students
	
_**Output Impedance**_  
Lower is better because the input impedance of the operational amplifier needs to be higher to prevent issues with overload.
	
Lower can mean more expensive though, so a balance needs to be found.
   
_**Additional Notes**_  
An operational amplifier will be needed to amplify the microphone output to get it to a level that is easier to work with. Further research may need to go into this, if we decide not to use something off-the-shelf.

_Reference Links_  
https://www.circuitbasics.com/what-is-a-microphone/  
https://mynewmicrophone.com/what-is-a-good-microphone-sensitivity-rating/  
https://www.neumann.com/homestudio/en/what-is-sensitivity  
https://www.neumann.com/homestudio/en/what-is-the-difference-between-electret-condenser-and-true-condenser-microphones  
https://mynewmicrophone.com/what-is-a-good-signal-to-noise-ratio-for-a-microphone/#:~:text=at%20the%20microphone.-,What%20is%20a%20good%20signal%2Dto%2Dnoise%20ratio%20for%20a,be%2079%20dB%20or%20more  

## Choice & Rationale

### Selection
Omnidirectional Microphone - [CMC-97450-44P](https://www.digikey.com/en/products/detail/cui-devices/CMC-9745-44P/6561041)  
Unidirectional Microphone - [DUM-4537L-HD-R](https://www.digikey.com/en/products/detail/pui-audio-inc/DUM-4537L-HD-R/16585493)  

Supporting Circuitry For Both:
- 2.2kOhm Resistor
- 1uF Capacitor

### Reasoning 
_Refer to issue #56 and the [Technology Report](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/Technology%20Report#microphone-options) for the other microphone examples._  
#### Why Two Microphone Choices?
An omnidirectional and a unidirectional microphone were selected for the final device design. The specific selection of one microphone will take place after the prototyping stage. The omnidirectional and unidirectional microphones will be tested to see which one will be best for the product we are attempting to develop.

#### Why the CMC-97450-44P?
The CMC-97450-44P microphone was selected for the omnidirectional option because it was a reasonable price and fit within our criteria for a microphone. The size is smaller compared to some of the other omnidirectional microphones that were suggested. Along with this, the voltage range is compatible with the standard logic voltage levels. The frequency range is between 20Hz and 20kHz, which overlaps with the typical range of 50Hz and 15kHz. The sensitivity is just below the expected range by 2dB, so it's still compatible with our requirements. The signal to noise ratio is a typical value of 60dB and the output impedance is a low enough value to work with (2.2kOhms). Originally, the omnidirectional microphone CMC-6035-130T was going to be selected. However, the CMC-6035-130T is dust tight and waterproof. These features are not needed for this product and it makes the microphone more expensive.

#### Why the DUM-4537L-HD-R?
The DUM-4537L-HD-R microphone was selected for the unidirectional option because it is the more affordable option price. All of the unidirectional microphone examples have very similar specification, so the selection was primarily made based on price. In addition to this, the size is larger compared to the PUM-2745L-HD-R option, which will be easier to work with. Along with this, the voltage range is compatible with the standard logic voltage levels. The frequency range is between 20Hz and 20kHz, which overlaps with the typical range of 50Hz and 15kHz. The sensitivity is within the typical range, so it's compatible with our requirements. The signal to noise ratio is a typical value of 68dB and the output impedance is a low enough value to work with (2.2kOhms).

#### Supporting Hardware
This hardware is the same for each microphone selection. The supporting hardware requirements were found in the datasheets for the microphones.

### Possible Challenges 

#### CMC-97450-44P
- The omnidirectional microphone will pick up student audio which may make the study material generation more difficult
  - However, this information may help generate better handouts since students are typically asking/answering questions when speaking in class
- In addition to student audio, the device may pick up non-conversational audio (e.g. papers moving, keyboard typing sounds, etc.)
  - This may only be an issue if students are sitting close to the device, so we may want to look into where this device will be placed in the classroom
- If we use a motor, the microphone may pick up the motor noise
  - This may not be an issue at all if we don't end up selecting a motor for the device
  - May not be the biggest issue since the motor noise may be pretty quiet

#### DUM-4537L-HD-R
- If an instructor is moving around the room, the audio may become more quiet and unintelligible 
  - This can be fixed by having the microphone follow the instructor or by having multiple microphones
  - The solution will require more hardware, which increase the final price of the design
  - The solution may also require more time to implement
- The unidirectional microphone options are more expensive compared to the omnidirectional microphone options, so this will increase the final design price
- May need to offer a way to adjust the direction the microphone is placed
  - The microphone may need to be pointed in a specific direction while the camera in another direction
  - This will be important to consider in the final device design
  - To combat this solution, more hardware and time may be needed to implement this solution


## Prototypes & Images
Was partially prototyped as a part of issue #1. Additional prototyping done as a part of [[Hardware] Microphone Test Report]([Hardware] Microphone Test Report).









