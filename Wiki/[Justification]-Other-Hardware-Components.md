[[_TOC_]]

## Selection
### Custom PCB
- Designing a custom PCB to connect all of the components that we have selected

### Battery Backup  
- None  

### Powering the Device  
- USB Type C Connector 

### Switches/Buttons
- [On/Off Slide Switch](https://www.digikey.com/en/products/detail/cw-industries/G-105-0513/1333) -> For camera enable/disable
- Reset Button -> On the Microcontroller

## Reasoning
### Custom PCB
We have decided to design our own PCB to connect all of the components that we have selected. We are not going to use a proto-board since a manufactured PCB will look more professional and may be more reliable. This will also allow us to design a board that works best for our design.

### Battery Backup
A battery backup will not be needed for this particular design since we are choosing to power the device using a USB A to USB C cable connected to a user's laptop. If the device is disconnected during a lecture, then a warning may be issued to the user through the application.

### Powering the Device
The components on our device either use a 3.3V or 5V power supply. Because we are using USB type C to transfer data, we will also be using this to power the device. The microcontroller that has been selected has a USB type C connecter that provides 5V and 3.3V power. This will be used to power the other components on the device.

### Switches/Buttons
A switch will be used to enable and disable the camera. This will provide the user with the ability to disable the camera if they would not like to use it during lecture. A standard on/off slider switch will be used for this. The microcontroller has a reset button connected to it, so we will not need to add one to our design.

## Possible Challenges 
- Without a battery backup, we may risk the loss of data during a lecture
  - We will try to prevent too much data from being lost by notifying the user as soon as possible
  - The product will be less expensive without a battery backup
- We will have to spend more time designing and reviewing the custom PCB
  - Proper scheduling will help prevent this from being an issue