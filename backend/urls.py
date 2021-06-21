from django.urls import path
from .viewsets.role import RoleViewSet
from .viewsets.user import UserViewSet
from .viewsets.group import GroupViewSet

urlpatterns = [
    
    # 角色管理
    path('backend/user/role/', RoleViewSet.as_view({'get':'list'})),
    path('backend/user/role/', RoleViewSet.as_view({'post':'create'})),
    path('backend/user/role/<int:pk>/', RoleViewSet.as_view({'delete':'destroy'})),
    path('backend/user/role/<int:pk>/', RoleViewSet.as_view({'put':'update'})),
    path('backend/user/role/<int:pk>', RoleViewSet.as_view({'get':'retrieve'})),

    # 用户管理
    path('backend/user/user/', UserViewSet.as_view({'get':'list'})),
    path('backend/user/user/', UserViewSet.as_view({'post':'create'})),
    path('backend/user/user/<int:pk>/', UserViewSet.as_view({'delete':'destroy'})),
    path('backend/user/user/<int:pk>/', UserViewSet.as_view({'put':'update'})),
    path('backend/user/user/<int:pk>', UserViewSet.as_view({'get':'retrieve'})),

    # 组管理
    path('backend/user/group/', GroupViewSet.as_view({'get':'list'})),
    path('backend/user/group/', GroupViewSet.as_view({'post':'create'})),
    path('backend/user/group/<int:pk>/', GroupViewSet.as_view({'delete':'destroy'})),
    path('backend/user/group/<int:pk>/', GroupViewSet.as_view({'put':'update'})),
    path('backend/user/group/<int:pk>', GroupViewSet.as_view({'get':'retrieve'})),

    
    
]