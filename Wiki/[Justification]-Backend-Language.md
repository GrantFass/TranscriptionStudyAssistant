# [Justification] Backend Language

## Potential Technology Options


<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Language</th>
    <th class="tg-0pky">Pros</th>
    <th class="tg-0pky">Cons</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"><a href="https://blog.back4app.com/backend-programming-languages-list/#10_NodeJS"><span style="color:#905">NodeJS</span></a></td>
    <td class="tg-0pky">- Allows for Object-Oriented Programming<br>- The Team should be familiar with this already<br>- Can be used in conjunction with other backends if needed<br>- NodeJS is decently fast to write<br>- Allows for quicker response times than running some websites locally</td>
    <td class="tg-0pky">- Cannot be multi-threaded at all</td>
  </tr>
  <tr>
    <td class="tg-0pky"><a href="https://levelup.gitconnected.com/"><span style="color:#905">QT C++</span></a></td>
    <td class="tg-0pky">- 20 years of support and lots of documentation<br>- Written in C++ so it is fast<br>- Widely used in industry for deploying on embedded systems<br>- Can run data intensive operations with type-safe methods<br>- secure and has advanced networking features<br>- integrate native engines for Android and IOS<br>- Has its own associated and responsive GUI language</td>
    <td class="tg-0pky">- Locks you into the QT ecosystem<br>- Hard to understand for the first time<br>- Requires its own IDE<br>- Hard to develop websites with it</td>
  </tr>
  <tr>
    <td class="tg-0pky">Ruby</td>
    <td class="tg-0pky">- object oriented<br>- multi-threaded<br>- mostly secure programming language (public encryption keys)<br>- Team is familiar with it<br>- faster than dynamic languages like Ruby.<br>- good dependency management with Maven and Gradle</td>
    <td class="tg-0pky">- slower than C++<br>- uses lots of memory<br>- not as portable to other platforms</td>
  </tr>
  <tr>
    <td class="tg-0pky">Java</td>
    <td class="tg-0pky">- Fast to write<br>- has classes and modules<br>- there are specific naming conventions for different variable types<br>- dynamic data typing</td>
    <td class="tg-0pky">- dynamic data typing<br>- slow at runtime<br>- somewhat limited documentation</td>
  </tr>
  <tr>
    <td class="tg-0pky"><a href="https://blog.back4app.com/backend-frameworks/#ASP_NET_Core"><span style="color:#905">ASP.NET Core</span></a></td>
    <td class="tg-0pky">- Somewhat fast to write</td>
    <td class="tg-0pky">- Locks you to C# and Windows I think</td>
  </tr>
  <tr>
    <td class="tg-0pky">Python</td>
    <td class="tg-0pky">- dynamic data typing<br>- same language that the ML models will be in probably<br>- Easy to code<br>- team has experience with it<br>- object oriented language<br>- platform independent language<br>- lots of libraries</td>
    <td class="tg-0pky">- can be slower than other languages like C++<br>- Dynamic data typing</td>
  </tr>
  <tr>
    <td class="tg-0pky">PHP</td>
    <td class="tg-0pky">- Its PHP<br>- one of the simplest backend programming languages<br>- commonly used, especially for web dev<br>- platform independent language<br>- loose typing<br>- interpreted language<br>- flexible and works with HTML, XML, and JS.<br>- Multiple PHP frameworks for web development</td>
    <td class="tg-0pky">- Its PHP<br>- loose typing<br>- interpreted language<br>- Not secure<br>- Poorly maintained<br>- not suitable for big projects<br>- inadequate error handling<br>- no dedicated libraries</td>
  </tr>
</tbody>
</table>

## Evaluation Strategies
One of the key things to keep in mind with our evaluation strategies is that this is a senior design project. This means that we have to make tradeoffs of performance in favor of development time. Below are some of the metrics we used for evaluation.
- Language familiarity
- Ease of writing endpoints
- Ease of reading and documentation
- Performance
- Some other requirements are that the ML models MUST be able to be linked to the backend. The backend must also be secure.

## Choice & Rationale
We ended up selecting Python as our backend language of choice. This choice was mainly made for the following reasons:
1. Python is a language that is familiar to most of the team. This means we do not need to learn a new language.
2. Python is really quick to write and has a lot of helper libraries. This will help aid in our development time. Faster development is necessary due to how much time we have spent on documentation and planning.
3. Machine Learning Integration. It is very easy to integrate the ML models directly into endpoints since they are both written in the same language.
4. Example code. The Machine Learning Production Systems CS topics course in the winter term ended up developing a REST application backend in python. This served as an ideal example for our backend and helped to greatly speed up development time.
5. Many of the python methods, especially those that use pandas, use numpy, or are vectorized have their backend written in c++ and are almost as fast as other languages.

## Prototypes & Images
We decided to prototype some of the backend as a part of issues #64, #65, and #66. These issues were more focused on the frontend though. Instead, some of the prototyping was put off until second semester. Second semester involved Grant taking the CS4981 ML Production Systems course which gave examples of how to integrate ML models with a backend. This mainly served as our prototyping to aid our decision. Another aspect of the prototyping was writing up an API document. This document contains everything that the backend should do. It can be found at [[Documentation] API Communication Protocol]([Documentation] API Communication Protocol).












