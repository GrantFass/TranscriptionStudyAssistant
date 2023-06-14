[[_TOC_]]

## Potential Technology Options

#### Camera Options  

| Name | Resolution | Frame Rate | FOV | Price (per unit) | Link |  
| ------ | ------ | ------ | ------ | ------ | ------ |  
| SVPRO USB Camera Board | 1080p | 30fps | Several Options (170 degree is the largest that's offered) | $52.99 - $41.99 | https://www.amazon.com/SVPRO-Fisheye-Windows-android-megapixel/dp/B07CSR2JZ3?th=1 |  
| Digilent Pcam 5C | 1080p | 30fps | Not specified - Fixed Focus | $44.99 | https://www.mouser.com/ProductDetail/Digilent/410-358?qs=f9yNj16SXrJa6gNGcCgCzg%3D%3D |  
| IMX219-130 | 8Mp | 30fps | 130 degrees (similar devices are offered with different field of views) | $29.44 | https://www.digikey.com/en/products/detail/seeed-technology-co.,-ltd/114992262/12396969?utm_adgroup=Seeed%20Technology%20Co.%2C%20LTD.&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_DK%2BSupplier_Tier%201%20-%20Block%202&utm_term=&utm_content=Seeed%20Technology%20Co.%2C%20LTD.&gclid=Cj0KCQjwhY-aBhCUARIsALNIC054BppzJoPhQpRiVsGWfFC9_3ZQfUSSg-PnbtXfVxu6g8-w6L9ozHsaApXHEALw_wcB |  
| LI-CAM-M034 Camera Module | 720p | 30fps | Not specified - M12 lens | $159.00 | https://www.mouser.com/ProductDetail/Leopard-Imaging/LI-CAM-M034?qs=8JtXMKbI7JSkH%252BRjczZhgw%3D%3D |  

## Evaluation Strategies
What needs to be taken into consideration:  
- Image Sensor Type
- Resolution
- Frame Rate
- Interfacing
- Field of View (FOV)  

_**Image Sensor Type**_  
There are two types of image sensor types: CDD (charged coupled device) and CMOS (complementary metal-oxide semiconductor). While CDD image sensors may provide lower-noise and higher-quality images, CMOS image sensors may be best for this particular project. CDD sensors are more expensive and require a larger amount of power to operate. Along with this, CMOS sensors are improving in quality and are a cheaper, more accessible option.  

_**Resolution**_  
The resolution of the camera is important because we want to provide clear videos to students. Most of the off-the-shelf devices provide 1080p or 2.1Mp resolution, so our goal is to provide a resolution similar to this.  

_**Frame Rate**_  
30fps (frames per second) will work for this application. For reference, most of the off-the-shelf conference devices have a frame rate of 30pfs.  

_**Interfacing**_  
This will be investigated in another section of this report. Some examples could be FireWire, USB, WiFi, etc.  

_**Field of View**_  
The instructor customer discovery survey results will be needed to determine the direction we would want to go with the field of view specification. If instructors would prefer to not have a wide-angle option for the camera, then we would select a camera with a smaller field of view (e.g. below 90 degrees). If instructors would a wide-angle option, then we would select a wide-angle camera (e.g. 90 degrees or above).  

_**References**_  
https://www.flir.com/support-center/iis/machine-vision/knowledge-base/key-differences-between-ccd-and-cmos-imaging-sensors/#:~:text=CCD%20sensors%20create%20high%2Dquality,transistors%20instead%20of%20the%20photosite  
https://www.phase1vision.com/blog/difference-between-cmos-and-ccd  
https://www.toradex.com/blog/choosing-the-right-image-sensor-for-embedded-iot-applications  

## Choice & Rationale
### Selection
- Main camera is [Arducam 5MP Plus OV5642 Mini Camera Module](https://www.sparkfun.com/products/18440)
- Backup camera is [SVPRO USB Camera Board - 2.8mm Lens](https://www.amazon.com/SVPRO-Fisheye-Windows-android-megapixel/dp/B07CSPB8SD?th=1)
- No supporting circuitry is needed.

### Rationale for Main Camera
Provides 5MP (2592x1944) resolution. The camera is meant to be interfaced with an Arduino, which means that we'd likely be able to use it with any FPGA we decided to use in the project.

Due to the camera using the SPI communication protocol, it should be easy to interface and retrieve data from it.

#### Specifications
- Resolution: 2592x1944/5MP, 1080p, 720p, VGA, QVGA
- Format Support: RAW, YUV, RGB, JPEG
- Frame Speed: ???
- Interface: SPI
- SPI Speed: Max 8MHz

### Rationale for Backup Camera
This camera was originally considered as primary before the discovery of the current primary. It was shunted to secondary for it's likely challenges of communicating via USB via sketchy protocols.

The selected camera provides 2.8mm focal length (approx $105^\circ$ FoV). The product itself is advertised as a camera which is 'plug & play' and boasts that it requires no drivers. the camera itself is also relatively small and can likely be mounted in the package we want to create.

Additionally, we already have the ability to get our hands on one via @Dr_K4rma's connection to Lunabotics, which has one we might be able to test out, so it's good to keep options open.

#### Specifications
- Resolution: 1080P/2MP
- Frame Speed: 30fps @ 1080P, 60fps @ 720P
- Interface: USB-A
- Size: 38x38mm or 32x32mm

### Challenges for Primary Camera
The main challenges that we'd likely be encountering would stem from the microcontroller that we end up choosing. We need to make sure we select one that has the proper hardware in order to implement the SPI communication protocol.

### Challenges for Backup Camera
The primary challenge will likely be interfacing with the camera. As it connects through USB, we'll need a micro-controller that is able to interface over USB, or that has the GPIO ports needed to jerry-rig such an interface.

Additionally, it's unknown how the camera actually interfaces with the computer it is connected to. As such, it's possible that the camera itself requires an OS-like environment to operate (i.e. OS-X, Linux, Windows), so if we use a microcontroller instead of a microcomputer, that could cause problems.

## Prototypes & Images
See #141


