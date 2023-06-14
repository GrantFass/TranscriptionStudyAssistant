# [Justification] Application Type

## Potential Technology Options
Below is a list of some resources information was gathered from:
- [denimdev.com](https://denimdev.com.au/blog/web-mobile-or-desktop/)
- [masstechnology.com](https://www.masstechnology.com/blog/2013/september/why-apps-reign-supreme/)  
- [arrowcore.com](https://arrowcore.com/blogs/web-mobile-or-desktop-app-which-is-right-for-your-project/)

### Mobile App
- Usually just run a website in a mobile aspect ratio
- Have to go through app store / IOS certification which costs money and sometimes has strict requirements.
### Desktop App
- More secure
- harder to deploy updates
- Need to make sure that the language works cross-platform
- can choose to use or not use outside dependencies 
- better performance
- no hosting costs
- better at ensuring data privacy
### Web App
- Can be a lot of outside dependencies that need to be validated
- outside dependencies can pose a security risk
- can be vulnerable to attacks
- lighter on computer resources
- can run on most hardware with a browser
- Needs an always active internet connection
- quicker updates
- no need to deal with app store / IOS certification
- no install needed.
- can work on mobile devices without certification for an app
- have to pay for server space
- slower than desktop apps
- API accessible from other applications
### Hybrid / Combination App
- can mix together the benefits of a mobile and web app while minimizing some of the downsides
- exact risks depend on exactly how the two applications are joined together.

## Evaluation Strategies
We plan to evaluate our choice based on the following parameters:
- How secure is the application? Does it have a lot of security risks?
- How easy is it to deploy updates to the software and machine learning models?
- How fast can the machine learning models run?
- Will a lot of space be required on the user's computer?
- Is it hard to install or setup the application?
- Cost
- Development complexity & time requirements

## Choice & Rationale
We plan to develop a web application. 

We started by removing mobile application from the possible candidates due to the cost and time of certification. We then removed the hybrid application due to the complexity and time required to develop it. This left the choice between web application and thick app.

We chose the web application over the thick application because it was better in almost every scenario. Below is a list of the evaluation strategies and how the application types stacked up. In that below list we can see that the web application was ahead or even in every field except for cost and security. 
| Evaluation Metric                | Thick App                                                                                                                                                                                                                                                                     | Web App                                                                                                                                                                                                                          |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application Security             | Application should be secure as there would be minimal outside connection to intercept.                                                                                                                                                                                       | Application needs to communicate over the web so all data that is sent must be encrypted, stored, and handled with care.                                                                                                         |
| Deployment & Update Ease         | Need a deployment pipeline defined. Would need to create an installer for different operating systems. Need to be able to uninstall old versions and install new versions. Would need some method of checking for new copies of the software and a place to download it from. | Just take the backend offline, pull new code from the repo, and restart. Simultaneously updates for all users.                                                                                                                   |
| Machine Learning Inference Speed | ML inference speed is constrained by local hardware. May cause thermal throttling and or take minutes on low grade hardware.                                                                                                                                                  | Can increase inference speed by improving the hardware the backend is deployed on. We control the hardware, and thus the inference speed.                                                                                        |
| Application Size                 | The application may be in the gigabytes size range since some of the machine learning models take up to 2gb all on their own. Additionally, the application may need to duplicate files that are uploaded to run in the background which would take more space.               | All of the size is on our own server. We can define how much space is used and available to each user.                                                                                                                           |
| Installation Complexity          | Application may be very complex to install as it would require a certified installer on different operating systems. If it was just a github installation then it would need some method of setting up databases and installing libraries on its own.                        | We can set up the environment however we need to in the backend and then it is applied for all users                                                                                                                             |
| Cost                             | There is minimal cost as the end users would be running the software locally.                                                                                                                                                                                                 | There is the cost of setting up a server with the appropriate hardware to run everything.                                                                                                                                        |
| Development Complexity           | Everything would be contained in the application and likely in the same language.                                                                                                                                                                                             | Needs two separate languages. One frontend language and one backend language. Backend language can be more tailored to machine learning.                                                                                         |
| Scalability                      | Hard to scale performance improvements as they are dependent on the users pc.                                                                                                                                                                                                 | Can scale performance improvements by using better hardware. For example, could go from a local server and object store to a parrelized server and object store in the cloud. An example would be using EC2 instances through AWS. |

## Prototypes & Images
This was partially prototyped as part of issues #64, #65, and #66. One of the applications (QT C++) was built more as a thick app. The other (Angular) was built more as a website. This helped to determine which would be easier.











