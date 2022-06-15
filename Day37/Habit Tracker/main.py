import requests
import datetime as dt

USERNAME = "javedalam"
TOKEN = "************************"
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# steps to create new user on pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.status_code
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# Creating a graph
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# coding_hour = int(input("Enter the Hours: "))
# date = #dt.datetime.now().date()
str_date = 20220615  # date.strftime("%Y%m%d")


# pixel_config = {
#     "date": f"{str_date}",
#     "quantity": f"{coding_hour}",
# }

# adding new pixel to the graph
post_pixel_endpoint = f"{graph_endpoint}/graph1"
# response = requests.post(url=post_pixel_endpoint,
#                          json=pixel_config, headers=headers)
# print(response.text)


# response = requests.put(
#     url=f"{post_pixel_endpoint}/{str_date}", json=pixel_config, headers=headers)
# print(response.text)

response = requests.delete(
    url=f"{post_pixel_endpoint}/{str_date}", headers=headers)
print(response.text)
