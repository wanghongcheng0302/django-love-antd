from django.urls import path
from .viewsets.permission import PermissionViewSet
from .viewsets.role import RoleViewSet
from .viewsets.user import UserViewSet
from .viewsets.group import GroupViewSet

urlpatterns = [
    
    # 权限组
    path('user/permission/', PermissionViewSet.as_view({'get':'list', 'post': 'create'})),
    path('user/permission/<int:pk>/', PermissionViewSet.as_view({'delete':'destroy', 'put':'update', 'get':'retrieve'})),

    # 角色管理
    path('user/role/', RoleViewSet.as_view({'get':'list', 'post': 'create'})),
    path('user/role/<int:pk>/', RoleViewSet.as_view({'delete':'destroy', 'put':'update', 'get':'retrieve'})),

    # 用户管理
    path('user/user/', UserViewSet.as_view({'get':'list', 'post': 'create'})),
    path('user/user/<int:pk>/', UserViewSet.as_view({'delete':'destroy', 'put':'update', 'get':'retrieve'})),

    # 组管理
    path('user/group/', GroupViewSet.as_view({'get':'list', 'post': 'create'})),
    path('user/group/<int:pk>/', GroupViewSet.as_view({'delete':'destroy', 'put':'update', 'get':'retrieve'})),

    
    
]