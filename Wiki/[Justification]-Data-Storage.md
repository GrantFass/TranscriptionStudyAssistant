# [Justification] Data Storage

## Potential Technology Options
There were a few potential options for data storage that we could use with the project.
| Technology Option   | Pros                                                                                                                                                                                                                                      | Cons                                                                                                                                                                          |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Local Storage       | Easy to develop with                                                                                                                                                                                                                      | Have to read from the local disc for every operation. Not organized. No security on files for various users. No scalability or redundancy.                                    |
| Relational Database | Takes up very little space in memory when they work properly                                                                                                                                                                              | Joins take a lot of time. Cannot store an entire relational database in memory. How does it make sense to split our data into smaller chunks to fit the relational paradigms. |
| NoSQL Database      | Can store all data in a single document.                                                                                                                                                                                                  | Can be slow. No real checks for file ownership.                                                                                                                               |
| Object Store        | Stores all data in a single document. Can have multiple documents. Can simulate paths and directories. Allow for checks of file ownership based on paths. Quicker than some other databases. Scalable with popular cloud options like AWS | Can be harder to setup and access.                                                                                                                                            |

## Evaluation Strategies
We plan to evaluate our choice based on a few criteria:
- how easy is it to check if a file belongs to certain users
- ease of accessing entire documents
- access speeds
- scalability
- Needs to be able to store JSON documents

## Choice & Rationale
We decided to go with Object Stores for storing log files and user data. This is mostly due to their ability to simulate paths and directories. Another reason is that we can develop with a local object store, such as MINIO, then scale to something larger, like AWS S3, when needed. One more reason is that the setup and access overhead was taken care of as a part of the Machine Learning Production Systems CS Topics course. 

## Prototypes & Images
This was mainly prototyped as a part of the CS4981 ML Production Systems course during Winter 2022-2023 at MSOE. This course helped to cover how some of the different database options work with deploying ML models and integration with backends.