import requests
from datetime import datetime
from credentials import pixela_token

USERNAME = 'andrerodpt'

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': pixela_token,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPHID = 'graph1'

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': 'graph1',
    'name': 'Running Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': pixela_token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

todays_date = datetime.now().strftime('%Y%m%d')

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
pixel_data = {
    'date': todays_date,
    'quantity': '3.21'
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_data, headers=headers)
# print(response.text)


pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{todays_date}"
pixel_data = {
    'quantity': '13.21'
}

# response = requests.put(url=pixel_put_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{todays_date}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)