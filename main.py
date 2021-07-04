import requests
from datetime import datetime

# Creating a user
token = "ayush1110"
user_name = "ayush10"

create_user_params = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url="https://pixe.la/v1/users", json=create_user_params)
# print(response.text)

http_verification = {
    "X-USER-TOKEN": token
}
graph_creation_end_point = f"https://pixe.la/v1/users/{user_name}/graphs"

graph_id = "ayush1110"

graph_params = {
    "id": "ayush1110",
    "name": "programming graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_creation_end_point, json=graph_params, headers = http_verification)
# print(response.text)

# updating graphs
today = datetime.now()
post_pixel_url = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_id}"
post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.5"
}


# response = requests.post(url=post_pixel_url, json=post_pixel_params, headers = http_verification)
# print(response.text)

# updating the graph pixel i.e using the requests module put function
update_pixel_url = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
update_pixel_params = {
    "quantity": "13"
}
# response = requests.put(url=update_pixel_url, json=update_pixel_params, headers=http_verification)
# print(response.text)

# deleting a pixel using the requests module delete function
response = requests.delete(url=update_pixel_url, headers=http_verification)
print(response.text)
