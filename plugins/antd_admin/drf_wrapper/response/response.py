from rest_framework.response import Response
from rest_framework import status


class RC:
    OK = 200


class DataPackage:
    """
    response结构标准化
    """

    def __init__(self, fields=None, elements=None, rc=RC.OK):
        self.fields = fields or dict()
        self.elements = elements or list()
        self.rc = rc

    def set_fields(self, fields: dict):
        """
        设置fields
        :param fields:
        :return:
        """
        self.fields = fields
        return self

    def set_elements(self, elements: list):
        """
        设置列表
        :param elements:
        :return:
        """
        self.elements = elements
        return self

    def set_field(self, key, value):
        """
        设置单个字段
        :param key:
        :param value:
        :return:
        """
        self.fields[key] = value
        return self

    def dumps(self):
        """
        输出data
        :return:
        """
        ret = dict()

        ret['fields'] = self.fields
        ret['elements'] = self.elements
        ret['rc'] = self.rc

        return ret


class JsonResponse:

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
