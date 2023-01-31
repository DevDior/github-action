from django.urls import path
from Test.views import TestAPIView

app_name='test2'
urlpatterns = [
    path('test', TestAPIView.as_view(), name='test'),
]