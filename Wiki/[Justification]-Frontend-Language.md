# [Justification] Frontend Language

## Potential Technology Options
| Language                | Pros                                                                                                                                                                                                                                       | Cons                                                                                                                                                                                                                                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| QML                     | Ways to add websites using [QT for webassembly](https://wiki.qt.io/Qt_for_WebAssembly). Used to create native embedded, desktop, and mobile applications. GUI can be in QTWidgets or QTQuick2. High Performance UI. Lots of documentation. | Requires the backend to be QT C++ or QT Python. Two language options causes confusion. Has to be developed using the proprietary QTCreator IDE. Model Delegate programming takes time to understand.                                                                                                              |
| JavaFX                  | Team has experience with it. Can be used to write cross platform applications. Basic XML GUI design. Has external libraries to help speed up some functions. Requires a thick app                                                          | Slow. No method to turn into a website and requires a thick app. Clunky and hard to work with. Not really an industry standard anywhere. Nesting can be complex. Not a lot of documentation for external packages. Some functions are locked behind unsafe external libraries. Hard to setup external JAR files. |
| HTML + CSS + JavaScript | Very lightweight. Free. Native support for most browsers. Easy to maintain. Team has experience.                                                                                                                                           | Hard to reuse code and does not follow DRY well. Hard to make dynamic pages. Have to test on multiple browsers. JS is not the most secure                                                                                                                                                                        |
| React                   | One of the most common JS libraries. Team should have a little experience with it. Can follow DRY. Lightweight virtual DOM.                                                                                                                | Developed by Facebook. Poor documentation. Changes very often.                                                                                                                                                                                                                                                   |
| Angular                 | Good for single page web applications. High performance and easy to install. Good out of the box functionality. Consistent                                                                                                                 | Can be complex and hard to understand                                                                                                                                                                                                                                                                            |
| Typescript              | Very similar to javascript. JS library support. Strict and structural typing with type hints.                                                                                                                                              | More effort than JS with no theoretical classes. Requires definition documents for external libraries.                                                                                                                                                                                                           |
| Vue                     | Very flexible. Create templates with JS. Can be learned after knowing react.                                                                                                                                                               | Too much flexibility causes confusion and complexity. Documentation is in Chinese.                                                                                                                                                                                                                               |
| Swift                   | Alternative to objective c with similar syntax. Preferred for iOS and OS X. Open source. Has good error prevention options                                                                                                                   | no backward support for iOS versions. Locks you to iOS somewhat.                                                                                                                                                                                                                                                 |
| Elm                     | easy to learn with lots of guides and compiler warnings.                                                                                                                                                                                   | Based on Haskell. No for loops. All functional programming. Cannot mutate values in nested structures. More restrictive than dynamic languages                                                                                                                                                                   |
| Node-Red                | good for very quick and dirty single page web app. Great for testing a backend.                                                                                                                                                            | Not meant to be deployed as a open web page. More for developer testing.                                                                                                                                                                                                                                         |


## Evaluation Strategies
Mostly going with what the software team wants to work with. Evaluating based on ease of use and development speed. The frontend language must be able to create a website GUI. It needs to be responsive. It also needs to be robust and secure.

## Choice & Rationale
Angular was chosen over other options such as QT C++. It was determined that QT was hard to use and not worth being locked into an ecosystem with. It would be easier to test a more traditional separated frontend and backend. Angular was then chosen over other options like react due to its consistency and performance.

## Prototypes & Images
We created minimal prototypes as a part of issues #64, #65, and #66. These created a simple GUI that allowed us to investigate how easy the languages were to use. The actual prototypes themselves can be found under the main code base of the repository.

Other Early Prototyping:
- [[Frontend] Early Possible Application Criteria]([Frontend] Early Possible Application Criteria)
- [[Frontend] Possible GUI Designs]([Frontend] Possible GUI Designs)