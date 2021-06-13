from rest_framework.response import Response
from rest_framework import status


class DataPackage(object):

    def __init__(self, fields=None, elements=None):
        self.fields = fields or dict()
        self.elements = elements or list()

    def set_fields(self, fields: dict):
        self.fields = fields
        return self

    def set_elements(self, elements: list):
        self.elements = elements
        return self

    def set_field(self, key, value):
        if not self.fields:
            self.fields = dict()
        self.fields[key] = value
        return self

    def dumps(self):
        ret = dict()

        if hasattr(self, 'fields'):
            ret['fields'] = self.fields

        if hasattr(self, 'elements'):
            ret['elements'] = self.elements
        return ret


class JsonResponse(object):

    def __new__(cls, status=status.HTTP_200_OK, data: DataPackage = None, headers: dict = None,
                msg: str = None, err: str = None):

        ret = dict()

        if data:
            ret.update(data.dumps())
        if msg:
            ret['message'] = msg
        if err:
            ret['error'] = err

        return Response(data=ret, status=status, headers=headers)
