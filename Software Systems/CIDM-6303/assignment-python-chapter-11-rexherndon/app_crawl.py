import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# Find all tags of <div class="s-post-summary">, which are questions by users
questions = soup.select(".s-post-summary")
for question in questions:
    # Inside all the <div class="s-post-summary">,
    # find the anchor tag with <a... class="s-link">
    # to get the text of the user's question
    question_text = question.select_one(".s-post-summary--content-title").getText()
    # find the anchor tag with <span class="s-post-summary--stats-item-number">
    #to get the number of votes the question has
    votes = question.select_one(".s-post-summary--stats-item-number").getText()
    print(question_text, votes)
print("---End Questions on page 1---")
"""
If you get an error of
    AttributeError: 'NoneType' object has no attribute 'getText'
the error means you spelled the class selector wrong
in .select() or .select_one()
soup cannot find any class with the wrong name.
Correct your spelling and try again.
"""

"""
Here are the URLs for page 2, 3, and 4. Notice a pattern?
https://stackoverflow.com/questions?tab=newest&page=2
https://stackoverflow.com/questions?tab=newest&page=3
https://stackoverflow.com/questions?tab=newest&page=4

We can build a loop to crawl through more pages.
"""

# start with page 2 since we already crawled page 1
for i in range(2, 5):
    url_suffix = f"?tab=newest&page={i}"
    next_url = url + url_suffix
    print(next_url)
    response = requests.get(next_url)
    soup = BeautifulSoup(response.text, "html.parser")
    for question in questions:
        # get the text of each question
        question_text = question.select_one(".s-post-summary--content-title").getText()
        # get the votes of each questions
        votes = question.select_one(".s-post-summary--stats-item-number").getText()
        print(question_text, votes)
print(f"---End Questions on page {i}---")