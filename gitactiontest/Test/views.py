from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):
    def get(self, request):
        print("Hello Test")
        return Response(True)
    
    def post(self, request):
        print("Hello Post")
        return Response(True)