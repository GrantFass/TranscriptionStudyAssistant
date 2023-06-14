## Sources
- A [Most Straightforward Explanation](https://www.youtube.com/watch?v=VrRV7hAKiIQ)
- B [Wiki Article](https://en.wikipedia.org/wiki/I%C2%B2S)
- C [Additional Information](https://www.allaboutcircuits.com/technical-articles/introduction-to-the-i2s-interface/)

## Brief
During development of the board, a question arose on whether or not to use the I2S protocol to setup communication between the microphones and the MCU. This investigation will provide information on this topic.

## TL;DR
I2S is completely irrelevant to the project at hand, as the microphones are pretty much wired directly to the MCU. The only case where I2S would be relevant would be if we were setting up a separate microphone which required anything above (ballpark) 1+ feet of cable.

## Original I2S Purpose
Before good cables like HDMI and DP became mainstream, many companies didn't have a good way to transfer digital data down a single wire. Granted, AV cables existed, but they weren't _one_ cable. So what people would do is multiplex and phase shift everything into one cable. As a result, the data could be transferred over one cable, but would suffer a massive decrease in quality.

Once modern, digital-oriented cables were developed, I2S was developed in order to facilitate the transfer of multi-channel audio via digital means.

## Expanded Result of Investigation
Because the microphones are located extremely close to the amplifier(s) and the MCU, there is no need for an I2S, as the signal will be converted to a digital format on the MCU itself