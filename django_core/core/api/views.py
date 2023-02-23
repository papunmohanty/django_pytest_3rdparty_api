from rest_framework.response import Response
from rest_framework.views import APIView

from .services import invoke_third_party_api

class ListViewStuffs(APIView):
    def get(self, request):
        location_id = 1
        response_data = invoke_third_party_api(location_id)
        # print(response_data)
        return Response({'message': response_data}, status=200)
