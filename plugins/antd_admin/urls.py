from django.urls import path
from .viewsets import LoginViewSet

urlpatterns = [
    path('login/', LoginViewSet.as_view({'post': 'login'})),
    path('logout/', LoginViewSet.as_view({'get': 'logout'})),
]
