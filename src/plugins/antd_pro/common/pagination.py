from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .response.response import DataPackage, JsonResponse


class AntdPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "pageSize"
    max_page_size = 100
    page_query_param = "current"

    def get_paginated_response(self, data):
        _d = DataPackage().set_elements(data)
        _d = _d.set_fields({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),

        })
        return JsonResponse(data=_d)


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    offset_query_param = "offset"
    limit_query_param = "limit"
    max_limit = 50

    def get_paginated_response(self, data):
        """
        定义分页器返回
        :param data:
        :return:
        """
        _d = DataPackage().set_elements(data)
        _d = _d.set_fields({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),

        })
        return JsonResponse(data=_d)
