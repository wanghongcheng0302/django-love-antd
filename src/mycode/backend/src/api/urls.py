from django.urls import path
from .viewsets import PermissionViewSet
from .viewsets import RoleViewSet
from .viewsets import UserViewSet
from .viewsets import GroupViewSet


urlpatterns = [
    # 权限管理
    path('user/permission/', PermissionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/permission/<int:pk>/', PermissionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # 角色管理
    path('user/role/', RoleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/role/<int:pk>/', RoleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # 用户管理
    path('user/user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # 组管理
    path('user/group/', GroupViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/group/<int:pk>/', GroupViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]