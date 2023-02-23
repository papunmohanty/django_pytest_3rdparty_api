from unittest.mock import patch
from rest_framework.test import APIRequestFactory

from core.api.views import ListViewStuffs


def test_list_view_stuffs():
    factory = APIRequestFactory()

    request = factory.get("/api/list/")

    with patch("core.api.services.invoke_third_party_api") as mock_invoke_api:
        mock_invoke_api.return_value = {
            "message": {
                "location_data": {
                    "location_id": 1,
                    "location_name": "Sample Location 1",
                    "address": "Address 1, for Shipment",
                    "latitude": 2.13,
                    "longitude": 7.89
                }
            }
        }
        view = ListViewStuffs.as_view()
        response = view(request)
        print(f"Respinse: {response.data}")
        assert response.status_code == 200
        assert response.data == {
            "message": {
                "location_data": {
                    "location_id": 1,
                    "location_name": "Sample Location 1",
                    "address": "Address 1, for Shipment",
                    "latitude": 2.13,
                    "longitude": 7.89
                }
            }
        }
