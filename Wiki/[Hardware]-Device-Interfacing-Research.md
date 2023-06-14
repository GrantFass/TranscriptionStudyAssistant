# Wired, Wireless, or Both  
For this particular device, we may want to go with a wired connection. It's important that connection isn't lost during lecture because it can result in the loss or corruption of lecture audio and video. It's less likely for a wired connection to become disconnected during lecture compared to a wired connection. For this reason, we probably should not use WiFi since the possibility of disconnection during lecture can be higher than a wired connection.

The minimum data rate for streaming 1080p video is 5Mbps. This is the video quality that we are attempting to provide, so we will need an interfacing option that can handle this data rate. Bluetooth has a maximum data rate range of 1-3Mbps, so this will also not be compatible with the transfer rate we need for 1080p video quality.

A wired connection will lower the chances of the device disconnecting from the laptop during the lecture, and can provide us with the data rate that we need for video streaming to a laptop.  

# USB Type C and USB Controller IC  
USB type C provides us with the ability to transfer audio, video, power, and data. This is good for our design since the device will need to transfer video and audio to a laptop. Along with this, it can support a 5Mbps data rate.

Some possible issues:
- This connector has more pins (24 pins for example)
  - Soldering will be more challenging
  - We will need to be able to support these pins as well
- This type of USB connector is more complex to work with, so more time may need to be allocated to getting this connector to work with our design

These issues will mostly take up time, so we would need to make sure we take this into consideration when creating our sprint schedules.

We will also need a USB controller IC to interface with the USB connector. The IC will need to have a data transfer rate of at least 5Mbps since this is what we need for 1080p video quality. The IC should handle the USB protocol and should be able to interface with a microcontroller. It should have the ability to interface with a USB type-C connector.

# Examples of USB Type C Connectors  
| Name | Manufacturer | Specifications | Max. Voltage | Max. Current | Price | Link |
| ---- | ------------ | -------------- | ------------ | ------------ | ----- | ---- |
| 2171840001 | Molex | USB 3.2 Gen 1 (USB 3.1 Gen 1, Superspeed (USB 3.0)) | 30V | 5A | $1.13 | https://www.digikey.com/en/products/detail/molex/2171840001/13913767?utm_adgroup=Connectors%2C%20Interconnects&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Supplier_Molex_0900_Co-op&utm_term=&utm_content=Connectors%2C%20Interconnects&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkptPK5fqABjA6ynW2lWIu46V18CQIXsr_nVQWXU5sG44RKECQKw63MaAjRHEALw_wcB |  
| 105450-0101 | Molex | USB 3.2 Gen 1 (USB 3.1 Gen 1, Superspeed (USB 3.0)) | 30V | 5A | $2.65 | https://www.mouser.com/ProductDetail/Molex/105450-0101?qs=P8zB4ONU6fyZ4amolPIupQ%3D%3D&mgh=1&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkpFNP-j_8lIDDdQ1gIBuuZKtjEWSu39OPQZttbJjySVcboC6JR-_nEaAqouEALw_wcB |  
| 632723130112 | Würth Elektronik | USB 3.2 Gen 2 (USB 3.1 Gen 2, Superspeed + (USB 3.1)) | 20V | 5A | $5.76 | https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/632723130112/10056481?utm_adgroup=USB%2C%20DVI%2C%20HDMI%20Connectors&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Connectors%2C%20Interconnects&utm_term=&utm_content=USB%2C%20DVI%2C%20HDMI%20Connectors&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkoeZiWvakoFhP1B8Ie96JviybVllFQQyfP3rqtllcmBVM-iirIbEvAaAuaBEALw_wcB |  

# Examples of USB Controller ICs
| Name | Manufacturer | Standard | Data Rate | Interface Type | Price | Link |
| ---- | ------------ | -------- | --------  | -------------- | ----- | ---- |
| FT233HPQ-TRAY | FTDI | USB-C 3.0 | 12Mbps | I2C/UART | $4.99 | https://www.mouser.com/ProductDetail/FTDI/FT233HPQ-TRAY?qs=DRkmTr78QAQsdVrZ8w%252Bb5g%3D%3D |  
| FT2233HPQ-TRAY | FTDI | USB-C 3.0 | 12Mbps | I2C/UART | $7.06 | https://www.mouser.com/ProductDetail/FTDI/FT2233HPQ-TRAY?qs=DRkmTr78QAStu2DOcegung%3D%3D |  
| FT4233HPQ-TRAY | FTDI | USB-C 3.0 | 12Mbps | I2C/SPI/UART | $8.07 | https://www.mouser.com/ProductDetail/FTDI/FT4233HPQ-TRAY?qs=DRkmTr78QASF%2FnlaHZtpVA%3D%3D |  

_One Main Difference -- the more expensive chips have more pins_

# USB-C to USB-A Cable Example
https://www.digikey.com/en/products/detail/seeed-technology-co.,-ltd/106990248/10290279?utm_adgroup=Seeed%20Technology%20Co.%2C%20LTD.&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_DK%2BSupplier_Tier%201%20-%20Block%202&utm_term=&utm_content=Seeed%20Technology%20Co.%2C%20LTD.&gclid=Cj0KCQiA4aacBhCUARIsAI55maEhd2-3psYhPQKvdeOf9BZlCeHp3RBgqIogpl39Yz4n3MicF94MVZIaAlw2EALw_wcB

# References
https://medium.com/@michalswoboda/usb-c-in-embedded-designs-practical-overview-17bed72da05a

https://tripplite.eaton.com/products/usb-connectivity-types-standards#:~:text=On%20newer%20devices%2C%20USB%E2%80%90C,resolution%204K%20and%208K%20video