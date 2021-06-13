from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):

    def get_permissions(self):
        action = getattr(self, 'action') if hasattr(self, 'action') else None
        if not action:
            action = list(getattr(self, 'action_map').values())[0]
        permission_classes = getattr(self, action).__dict__.get('permission_classes')
        if permission_classes:
            return permission_classes
        return super(BaseModelViewSet, self).get_permissions()

    def get_authenticators(self):
        action = getattr(self, 'action') if hasattr(self, 'action') else None
        if not action:
            action = list(getattr(self, 'action_map').values())[0]
        authentication_classes = getattr(self, action).__dict__.get('authentication_classes')
        if authentication_classes:
            return authentication_classes
        if isinstance(authentication_classes, tuple) and len(authentication_classes) == 0:
            return authentication_classes
        if authentication_classes is None:
            return ()
        return super(BaseModelViewSet, self).get_authenticators()

    def get_throttles(self):
        action = getattr(self, 'action') if hasattr(self, 'action') else None
        if not action:
            action = list(getattr(self, 'action_map').values())[0]
        throttle_classes = getattr(self, action).__dict__.get('throttle_classes')
        if throttle_classes:
            return [throttle() for throttle in throttle_classes]
        return super(BaseModelViewSet, self).get_throttles()
