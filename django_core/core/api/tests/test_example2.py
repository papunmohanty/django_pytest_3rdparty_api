import json
from unittest.mock import patch, Mock

import pytest
from rest_framework.test import APIRequestFactory

from core.api.views import ListViewStuffs


@pytest.fixture
def mocked_invoke_third_party_api():
    with patch("core.api.views.invoke_third_party_api") as mock_invoke:
        yield mock_invoke


def test_list_view_stuff2(mocked_invoke_third_party_api):
    factory = APIRequestFactory()
    request = factory.get("/api/list/")
    listings = {
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
    mocked_invoke_third_party_api.return_value =  {
            "location_data": {
                "location_id": 1,
                "location_name": "Sample Location 1",
                "address": "Address 1, for Shipment",
                "latitude": 2.13,
                "longitude": 7.89
            }
        }

    view = ListViewStuffs.as_view()
    response = view(request)
    print(f"Response2: {response.data}")
    print(f"listings: {listings}")
    assert response.status_code == 200
    assert response.data==listings
