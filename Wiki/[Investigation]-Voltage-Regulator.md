## Result
A voltage regulator is unneeded, Rev 2 of the circuit for handling the microphone(s) was incorrect.

Reference the below sections for an explanation for an alternative solution.

Additionally, we might be able to combine issue #154 and #155 due to the nature of the solution.

## Research
Voltage regulator is **NOT** needed. Our original circuit for the unidirectional mic was incorrect... Might be the same for the omnidirectional mic too, actually.
Issue documentation was changed after meeting with Dr. Faulkner.

### Why Old Circuit Didn't Work
There were two big mistakes made in the previous circuit which lead to this problem. They were:
1. The assumption that voltage dividers work in all cases.
2. The assumption that the microphone only consumes voltage and outputs a variation.

In fact, the microphone not only uses consumes voltage (to power internal circuitry), but _also_ drives current. This is significant because voltage dividers do not work in the presence of current drivers.

If we take the original schematic and simplify it a bit (getting rid of irrelevant parts), we're left with this:
![image](/uploads/4c75680a9a1b867a2c504769143fa702/image.png)

Now, if we highlight the pathway the current will take, we can calculate a couple interesting values. Most notably, how much voltage we would actually need to make this work (more or less).

![image](/uploads/f9a1b90c0409d26f4717fb6ede00e97c/image.png)

Since the microphone actively drives the current when active, we use the equation $`v=ir`$ to calculate the voltage needed, where $`i=500\mu A`$ (driving current found on the datasheet) and $`r=100k\Omega+2.2k\Omega`$. So $`V=51.1V`$. In other words, we'd need to have a 51.1V bus to make this work, which isn't feasible.

To solve this problem, we should use the circuit found in the next subsection, which addresses these problems.

### New Circuit
![image](/uploads/1212b0d247d994c276c61c864d085a2e/image.png)

This circuit might seem overcomplicated and nonsensical, but let's break it down.

![image](/uploads/6c0550e2d1e3b7c62499fddb505e56eb/image.png)

#### Part A
This is the basic microphone assembly. It provides the necessary current and voltage (and current!) to make this work. Using the same equations as before, $`v=ir=1.1V`$, here we can see that we can even bump up the resistance to give a better audio quality. If we want to use 3.5V (leaving 1V for microphone use and 0.5V for breathing room), we can bump up the resistance to $`r=\frac{v}{i}=7k\Omega`$.

Keep in mind that the output of this part (which exits right) will output a signal of approximately $`v\approx5\pm5\mu V`$, where the 5 volts is the DC component and the $`5\mu V`$ is the analog component.

#### Part B
This receives the signal from the microphone output and removes the analog component. So at the end of this operation, the signal ends up being $`V\approx\pm5\mu V`$. This is fed into the next part.

#### Part C
This is a voltage divider, however because there are no current drivers here, it will work as intended, which is to re-introduce the DC component to the signal, resulting in the signal being $`V\approx2.5V\pm5\mu V`$. It's important for the signal to be directly in between the high voltage value (5V) and low/reference voltage value (0V). This then feeds into the next part.

#### Part D
This part takes the miniscule differences ($`\sim5\mu V`$) that the microphone originally output and stretches it to the bounds of the voltage spectrum, resulting in the signal being much bigger, not to mention interpretable by the MCU's ADC.

All in all, this is a good guideline for what the final circuit should look like, but should still be tested for optimal values.

### Additional Point(s)
#### 2V Mic on 5V
According to Dr. Faulkner, since the documentation lists the mic's operating voltage as anywhere from 2-10V, plugging it into the 5V bus should be completely fine and would result in a miniscule loss in audio quality at worst.