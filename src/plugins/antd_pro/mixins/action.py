from abc import abstractmethod


class ActionMixin:
    """
    让组件具备接口调用能力
    """
    button = '操作'
    method = 'post'
    name = ''

    @abstractmethod
    def service(self, request, *args, **kwargs):
        pass
