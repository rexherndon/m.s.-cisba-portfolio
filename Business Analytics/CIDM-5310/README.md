# Disclaimer:

This assignment was originally intended as the final project for my “Business Intelligence and Decision Support Systems” class (CIDM-5310) taught by Dr. Jeffry Babb at West Texas A&M University in the Summer I semester. Since then, this assignment has been published to this GitHub repository as a part of developing my portfolio for my M.S. Computer Information Systems and Business Analytics Capstone Course (CIDM-6395), which is also taught by Dr. Jeffry Babb. 

This repo does not contain the entire project, since some files of this project have been corrupted or are missing after the original project was submitted. Samples of the project found in the repo still substantiate and provide enough context for the work of the original project.

# BILC Final Project Summary

For this project, I explored and analyzed two datasets that were taken from NYC Open Data. These data frames are records of each motor vehicle collision recorded by NYPD between March 2016 and December 2021, with some outlier records even going as far back as 2012. Each record contains detailed crash information, including information such as vehicles involved, casualties/injuries, location of each incident, vehicle damage, date and time, etc. The links for the data containing the records of the crashes and the vehicles can be found here:

[Motor Vehicle Collisions - Crashes | NYC Open Data](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)

[Motor Vehicle Collisions - Vehicles | NYC Open Data](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Vehicles/bm4k-52h4)

For this analysis, I wanted to identify the current state of motor vehicle collisions in densely populated urban areas, such as New York City. I wanted to retrieve information such as common reasons for vehicle collisions, the impact of them (ie. identifying casualties or injuries), common times for collisions to occur, and common vehicle types. The primary reason for doing this would be to visualize this information to other governments in urban areas and even stakeholders/executives for motor vehicle companies to help contribute to the reduction of motor vehicle collisions and car accidents in the future.

I asked/answered the following questions to help guide me along my analysis.

- What percentage of overall collisions lead to one or more injuries/fatalies?
- What are the primary contributing factors for vehicle collisions?
- Do vehicle collisions happen more during AM times or PM times?
- What is the main vehicle type involved in a collision?

I chose these datasets due to their availability and compatibility with each other. The two datasets contained a combined total of almost 5 million records before cleaning the dataset. In this particular project, availability is more important than applicability, and I wanted to tie my questions in with the data that I already had so I could get the best results on what I could look for. I also picked this pair of datasets because they were both made by the NYPD, and they both relate to each other, so there are ways I join the data easily and find what I am looking for. In addition, the columns they have provided for each dataset are very useful and Pandas can allow me to easily preprocess and work with the data to find answers to my given questions. Also, I recently found out that NYPD is continually updating this data once every few years, but this is the most relevant data available to the public. This data is also important because we are getting this information from a primary source, and datasets like this would give us valuable information within our given context.

The tools I have included in my BI dashboard and Jupyter Notebook include the following:

- Preprocessing tools (dropping unneeded columns or rows/cols where null data is found)
- Aggregations and Grouping tools to sort by categories
- Tools to interpolate or resample data to assist with identifying trends
- Tools to manipulate datetime or timedelta objects
- Tools to plot different graphs (ie. Matplotlib) (line, bars, histograms, etc.)

Note: All of these tools, with the exception of plotting and graphing, are found in the Pandas package.

With the answers I have found from my BI dashboard, I hope to use this material to contribute to the reduction of motor vehicle collisions in densely populated urban environments. I hope to be able to reach out other local governments in other urban environments, the federal government, or stakeholders/executives of common motor vehicle companies to reinforce the importance of motor vehicle safety. I also hope to direct further attention to developing technologies or rules centered around common factors of a motor vehicle collision.
