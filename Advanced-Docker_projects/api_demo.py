import requests

# API URL
url = "https://randomuser.me/api/"

# API ko request bhejna
response = requests.get(url)

# Response ko JSON format me convert karna
data = response.json()

# Required information nikalna
user = data["results"][0]

name = user["name"]["first"] + " " + user["name"]["last"]
email = user["email"]
country = user["location"]["country"]

# Print output
print("Name :", name)
print("Email :", email)
print("Country :", country)