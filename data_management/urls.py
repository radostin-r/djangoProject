from django.urls import path
from .views import MessageView

urlpatterns = [
    path('data/', MessageView.as_view(), name='data'),
]
