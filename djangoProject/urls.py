from auth_service.urls import urlpatterns as auth_service_urls
from data_management.urls import urlpatterns as data_management_urls

urlpatterns = auth_service_urls + data_management_urls
