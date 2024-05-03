# Data Mining and Management Overview

This folder contains my written appraisal for the Data Mining and Management curriculum area in the Master of Computer Information Systems and Business Analytics (MS CISBA) degree program. It goes through the classes I have taken within the curriculum, what they have taught me, the strengths and weaknesses I have regarding this knowledge area, samples of the work I have done within these classes, and any future developments I wish to make related to this knowledge area.

In the Data Mining and Management curriculum area, I have taken two courses:

- CIDM 6351 - Business Data Extraction, Transformation, and Load
- CIDM 6355 - Data Mining Methods

During that time, I produced different artifacts of work showcasing the knowledge and skills developed in this curriculum area. These artifacts can be found in three different repositories, but I have also taken the time to copy the contents from those repositories into sub-folders within this repository as well (to keep everything consolidated).

- [https://github.com/rexherndon/cidm-6351-artifact](https://github.com/rexherndon/cidm-6351-artifact)
- [https://github.com/rexherndon/cidm-6355-artifact](https://github.com/rexherndon/cidm-6355-artifact)

The CIDM-6351 artifact is the final exam of this class, and it tested my ability to extra data from a few different data sources (like JSON, CSV, and SQLite database files), clean them, and create queries for further analysis.

The CIDM-6355 artifact is a report created as part of a group project where we tested different data models to identify which data mining/machine learning model would be the best for creating an email spam filter, given a dataset of several thousand records of spam and legitimate emails for training.

Regarding the Data Mining and Management knowledge area synthesis in my application, I was advised by Dr. Sen to create documentation going over the business rules of Chordity and an Entity Relationship Diagram (ERD) showcasing how the models/entities in my application interact with each other. This was created as another form of application hardening to ensure no data is vulnerable to a leak or exploit. During the development of my application, I started by creating an ERD and then coding the models in my application to ensure they were properly implemented. Also, within this area, I upgraded the database from the default SQLite database that Django provides to a PostgreSQL database, which is more robust for production environments. This database is also currently hosted on the cloud by Render.