import requests  
# Importing the requests library. This library helps us send requests to an API and receive data from it.


# API URL
url = "https://randomuser.me/api/"
# Storing the API address in a variable called 'url'.
# This API provides random user information like name, email, and country.


# Sending request to API
response = requests.get(url)
# Sending a GET request to the API URL.
# The API server receives our request and sends back user data.
# The returned data is stored in the 'response' variable.


# Converting response into JSON format
data = response.json()
# The API sends data in JSON format.
# This line converts JSON data into a Python dictionary so we can easily access the information.


# Extracting the first user data from the results list
user = data["results"][0]
# The API response contains user information inside the "results" list.
# [0] means we are selecting the first user from the list.


# Getting user's full name
name = user["name"]["first"] + " " + user["name"]["last"]
# Extracting the first name and last name from the user data.
# Adding both names with a space to create the complete name.


# Getting user's email address
email = user["email"]
# Extracting the email address from the API response and storing it in the email variable.


# Getting user's country name
country = user["location"]["country"]
# Accessing the location information and extracting the user's country.


# Displaying the output
print("Name :", name)
# Printing the user's full name on the screen.


print("Email :", email)
# Printing the user's email address on the screen.


print("Country :", country)
# Printing the user's country on the screen.