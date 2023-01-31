from django.urls import path
from .views import TestAPIView

app_name='test'
urlpatterns = [
    path('test', TestAPIView.as_view(), name='test'),
]
