from rest_framework.viewsets import ModelViewSet as _ModelViewSet


class ModelViewSet(_ModelViewSet):

    def get_serializer(self, *args, **kwargs):
        fields = getattr(self, 'fields', None)
        exclude = getattr(self, 'exclude', None)
        context = getattr(self, 'context', {})
        return self.serializer_class(fields=fields, exclude=exclude, context=context, *args, **kwargs)

    def get_permissions(self):
        action = getattr(self, 'action') if hasattr(self, 'action') else None
        if not action:
            action = list(getattr(self, 'action_map').values())[0]
        permission_classes = getattr(self, action).__dict__.get('permission_classes')
        if permission_classes:
            return permission_classes

        return super(ModelViewSet, self).get_permissions()

    def get_authenticators(self):
        action = getattr(self, 'action') if hasattr(self, 'action') else None
        if not action:
            action = list(getattr(self, 'action_map').values())[0]
        authentication_classes = getattr(self, action).__dict__.get('authentication_classes')
        if authentication_classes:
            return [_class() for _class in authentication_classes]

        return super(ModelViewSet, self).get_authenticators()

    def get_throttles(self):
        action = getattr(self, 'action') if hasattr(self, 'action') else None
        if not action:
            action = list(getattr(self, 'action_map').values())[0]
        throttle_classes = getattr(self, action).__dict__.get('throttle_classes')
        if throttle_classes:
            return [throttle() for throttle in throttle_classes]
        return super(ModelViewSet, self).get_throttles()
