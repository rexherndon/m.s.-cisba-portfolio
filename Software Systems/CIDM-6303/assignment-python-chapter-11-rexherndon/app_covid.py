import requests
"""
Documentation at 
https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""

# 1. get the API data from the web server
# This API server does not require an API key
# 2. Convert the data into a useful python objects: usually a list or dictionaries
url = "https://api.covid19api.com/summary"

response = requests.get(url)
data = response.json()

global_stats = data['Global']

deaths = global_stats['TotalDeaths']
cases = global_stats['TotalConfirmed']
mortality_rate = deaths / cases
print(f"Total Deaths: {deaths:,}\nTotal Confirmed Cases: {cases:,}\nMortality Rate: {mortality_rate:.3f}")

# import requests
# import config
# # Get data from Yelp using API calls
# # Need to watch Mosh' video 10.4 AND 10.5 to understand this code.
# # Dr. Humpherys added different ways to filter and loop through the data

# url = "https://api.yelp.com/v3/businesses/search"
# # Note: Yelp allows the key:value pairs to be lowercase or uppercase
# # Notice the "bearer " as a space inside quotes. YELP expects the space.
# # or a validation error will occur.
# headers_dictionary = {
#     "authorization": "bearer " + config.api_key
# }
# params_dictionary = {
#     "term" : "barber",
#     "location" : "nyc"
# }
# response = requests.get(url, headers=headers_dictionary,
#                         params=params_dictionary)
# # Convert the json object to a dictionary
# result = response.json()

# # return the value of the dictionary key "businesses"
# businesses = result["businesses"]
# print(type(businesses))
# # Note: The businesses variable is a list containing dictionaries where each dictionary contains data regarding one business. Dictionary keys are case sensitive. business["name"] != business["Name"]
# for business in businesses:
#     print(business["name"], business["rating"], business["review_count"])



# print("-"*30)
# # Use string interpolation to format the output
# for business in businesses:
#     # Must use single quotes inside the dictionary['key_name'] because business['name'] is inside the double quotes of the string interpolation.
#     print(f"Name: {business['name']}. Avg Rating: {business['rating']}")



# print("-"*30)
# print("---Businesses with reviews >= 4.5")
# # Use list comprehension to filter the data using one line of code. names is a list of strings
# names = [business["name"]
#         for business in businesses if business ["rating"] >= 4.5]
# print(names)