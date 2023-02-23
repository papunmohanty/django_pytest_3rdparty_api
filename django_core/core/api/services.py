import requests


def invoke_third_party_api(location_id: int):
    API_ENDPOINT = "http://127.0.0.1:8001/"
    params = {"location_id": location_id}
    response = requests.get(API_ENDPOINT, params=params)
    # if response.ok:
    return response.json()
    # else:
    #     return None
