[[_TOC_]]

## Potential Technology Options

### [Hardware to Software Communication Interface](https://www.techtarget.com/iotagenda/tip/Top-12-most-commonly-used-IoT-protocols-and-standards)
- [Hardware Engineering Design: Digital Communications Overview](https://www.hwe.design/design-fundamentals/digital-communication-interface-basics)
- [Hardware Engineering Design: Digital Communications Low Speed](https://www.hwe.design/design-fundamentals/digital-communication-interface-basics/low-speed)
- [Hardware Engineering Design: Digital Communications High Speed](https://www.hwe.design/design-fundamentals/digital-communication-interface-basics/high-speed) 
#### Wired Options
- USB (Type C, Type B, Micro-B, Type A)
  - Should be really easy to connect to
  - Works with a lot of devices.
  - If we just put a port on the device and provide a cable it lets consumers change the cable if needed
  - [Speeds](https://en.wikipedia.org/wiki/USB)
    - USB 3.0 - 5 Gbps
    - USB 3.1 - 10 Gbps
    - USB 3.2 - 20 Gbps
    - USB4 - 40 Gbps
- Ethernet (IEEE 802.3)
  - Speeds
    - CAT-6 - 1 Gbps @ 250MHz
    - CAT-6a -10 Gbps @ 500MHz
    - CAT-7 - 10 Gbps @ 600MHz
    - CAT-8 - 40 Gbps @ 2GHz
  - Would not work with most ultrabooks as they have no Ethernet port
- Serial / Firewire
  - ?
#### Wireless Options
- Cellular
  - Has a limitation when inside buildings
- Wi-Fi (IEEE 802.11)
- Bluetooth (IEEE 802.15.1)
- ZWave / Zigbee (IEEE 802.15.4) / Other
  - Most of these are IoT specific and will be hard to communicate with for most.

## Evaluation Strategies
- Ease of programming
- Ease of installation
- Transfer / Communication speeds
- Connection Stability
- Connection Security
- Cost of relevant hardware (ports, communication chips, drivers, etc)

## Choice & Rationale
Wired Connection -> USB Type C  

### Reasoning

For this particular device, we may want to go with a wired connection. It's important that connection isn't lost during lecture because it can result in the loss or corruption of lecture audio and video. It's less likely for a wired connection to become disconnected during lecture compared to a wired connection. For this reason, we probably should not use WiFi since the possibility of disconnection during lecture can be higher than a wired connection.

The minimum data rate for streaming 1080p video is 5Mbps. This is the video quality that we are attempting to provide, so we will need an interfacing option that can handle this data rate. Bluetooth has a maximum data rate range of 1-3Mbps, so this will also not be compatible with the transfer rate we need for 1080p video quality.

A wired connection will lower the chances of the device disconnecting from the laptop during the lecture, and can provide us with the data rate that we need for video streaming to a laptop.  

USB type C provides us with the ability to transfer audio, video, power, and data. This is good for our design since the device will need to transfer video and audio to a laptop. Along with this, it can support a 5Mbps data rate.

### Possible Challenges 
- This type of USB connector is more complex to work with, so more time may need to be allocated to getting this connector to work with our design
  - This issue will mostly take up time, so we would need to make sure we take this into consideration when creating our sprint schedules

## Prototypes & Images
Prototyped as a part of [[Hardware] Device Interfacing Research]([Hardware] Device Interfacing Research).







