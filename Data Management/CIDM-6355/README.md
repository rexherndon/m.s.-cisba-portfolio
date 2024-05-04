# Disclaimer:

This assignment was originally intended as the final project for my “Data Mining Methods” class (CIDM-6355) taught by Dr. Liang (Leon) Chen at West Texas A&M University in the Fall 2023 semester. Since then, this assignment has been published to this GitHub repository as a part of developing my portfolio for my M.S. Computer Information Systems and Business Analytics Capstone Course (CIDM-6395) taught by Dr. Jeffry Babb. 

This group project consists of contributions made by myself, alongside my other colleagues, Cecilia Foy, Brandon Koch, Mohammadsalim Shaikh, and Jordan Unfred.

# Spam Email Detection Report - Executive Summary:

Email has become a nearly universal form of communication and identification over the
past few decades, and it’s seemingly tied to just about every single service we use on the web,
from newsletters to applications, to account registrations, and so many more options. “Despite
the growing popularity of messengers, chat apps, and social media, email has managed to
remain at the center of digital communication and continues to grow every year” (Damar, p.
184).
This report was created with the intention to assist with the development of spam filters,
and their purpose of reducing spam appearing in people’s inboxes. Our goal is to identify the
most efficient data mining and classification method for creating an effective spam filter. The
data provided below offers insight into the different characteristics of spam/legitimate emails in
our “Spambase” dataset. Our data analysis programs, RapidMiner and R/RStudio were used to
create different data mining models, run predictive analysis on the testing portion of our dataset,
and perform model evaluation to compare and identify the best model/data mining method for
our intended goal. Models used such as Decision Trees, Neural Networks, Naive Bayes, and
Logistic Regression provide detailed information about spam detection and prediction.
From our efforts, we have concluded that our Naive Bayes model in R/RStudio (Model
4) gave us the best results compared to every other classification method we used in our
analysis based on overall accuracy, recall, and precision, especially in determining true values
(ie. – where “class” = 1, which is our label for a spam email) between the training and testing
sections of our dataset. This model was chosen, since it had the highest precision percentage for
identifying spam emails compared to our other 7 models. Precision is a more important measure
when the cost or stakes of creating a false positive is greater than the cost or stakes of creating a
false negative. If our spam filter sent a false positive (ie. - a spam email to a user’s main inbox)
and the user clicked on it, the consequences could be range from annoying to devastating, since
these spam emails could retrieve information about a particular user and either leak it publicly if
it is personal information or sell this information to companies with malicious or immoral
intent, such as targeted advertising or phishing. If these spam emails were also a phish that the
user fell for since it would appear as a legitimate email, these senders could obtain usernames
and passwords, financial information, or other sensitive personal information to use for
blackmail, harassment, or identity theft.
Based on our findings, we would like to reach out to larger email providers, such as
Google (Gmail), Yahoo/RocketMail, or ProtonMail, and collaborate with them to integrate our
findings into their existing spam filters. The war against spam and phishing emails is one that
we can never truly win, as companies work tirelessly to find different ways to reduce or
eliminate spam emails from user’s inboxes every single day. We hope that our contributions
through our data mining methods defined in this report can help with the reduction of spam in
user’s inboxes.
Some limitations with our data were with the overall size of our data (4601 records) and
with the age of the dataset itself. This might make our data irrelevant from some perspectives,
but for the case of this report, the data that we have is still a great starting point for the
development of our data mining models throughout the entire data mining process, and this can
be backed up by the fact that this dataset is still cited in several peer-reviewed articles, with
several of the most recent articles and reports being published as recent as 2019.
