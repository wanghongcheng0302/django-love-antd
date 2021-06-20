from django.urls import path
from .viewsets import LoginViewSet, UserViewSet

urlpatterns = [
    path('login/', LoginViewSet.as_view({'post': 'login'})),
    path('userDetail/', UserViewSet.as_view({'get': 'user_detail'})),
]
