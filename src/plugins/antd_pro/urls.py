from django.urls import path
from .views import AntdPermissionViewSet, AntdRoleViewSet, AntdUserViewSet, LoginViewSet, AntdCasbinRuleViewSet, \
    AntdMenuRuleViewSet

urlpatterns = [
    # 权限管理
    path("permission/", AntdPermissionViewSet.as_view({"get": "list", "post": "create", 'delete': 'batch_destory'})),
    path("permission/<int:pk>/",
         AntdPermissionViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # 角色管理
    path("role/", AntdRoleViewSet.as_view({"get": "list", "post": "create", 'delete': 'batch_destory'})),
    path("role/<int:pk>/", AntdRoleViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), ),

    # 用户管理
    path("user/", AntdUserViewSet.as_view({"get": "list", "post": "create", 'delete': 'batch_destory'})),
    path("user/<int:pk>/", AntdUserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), ),

    # casbin管理
    path("casbin/", AntdCasbinRuleViewSet.as_view({"get": "list", "post": "create", 'delete': 'batch_destory'})),
    path("casbin/<int:pk>/",
         AntdCasbinRuleViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), ),

    # 菜单管理
    path("menu/", AntdMenuRuleViewSet.as_view({"get": "list", "post": "create", 'delete': 'batch_destory'})),
    path("route/", AntdMenuRuleViewSet.as_view({"get": "fetch_routes"})),
    path("menu/<int:pk>/",
         AntdMenuRuleViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), ),

    # 登陆
    path("login/", LoginViewSet.as_view({"post": "login"})),
    path("currentUser/", LoginViewSet.as_view({"get": "current_user"})),
]
