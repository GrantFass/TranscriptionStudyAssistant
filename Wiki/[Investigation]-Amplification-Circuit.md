## Sources
- A: [Amplification Circuit](http://www.learningaboutelectronics.com/Articles/Microphone-amplifier-circuit.php)
- B: [Amplification Breakout Board](https://www.adafruit.com/product/2130)

## Brief
Due to the low-voltage response of the two microphones, an additional amplification circuit needs to be put in between the microphone(s) output and the MCU (Main Control Unit) inputs.

## Prototyping Solution
The amplification circuit is simple in design, but would still add unneeded overhead during the prototyping phase. As such, a breakout board will be utilized for the time being. Reference `Source B`.

## End-Product Solution
While the prototyping solution is simple in implementation, the breakout board is much bigger than necessary due to the typical nature of it's use-case (prototyping and hobby-ing). Because the circuit being is simple, and because the breakout board is larger than necessary, the final product should integrate this circuit into the main PCB. For this, reference `Source A`.

## Additional Points
### Dedicated Amplification Chips
Audio amplification chips exist. However, most of the ones considered were high-end, 50-something pin chips which do additional audio processing and are likely more complex (not to mention more expensive) than what we need or can support with the current MCU.

### Noise Filtering
The amplification circuit is a **voltage** amplification circuit. There is nothing there that specifically looks for audio. As such, any other noise on the wire will also be amplified, such as thermal and coupling noise. This additional noise filtering will need to be done either through software, or through additional hardware filters (pending testing).