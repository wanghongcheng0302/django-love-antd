from rest_framework.renderers import JSONRenderer
from .response import DataPackage
from rest_framework.exceptions import ErrorDetail, ValidationError


class Renderer(JSONRenderer):

    @classmethod
    def check_error(cls, value):
        if isinstance(value, list):
            for item in value:
                cls.check_error(item)
        if isinstance(value, dict):
            for k, v in value.items():
                cls.check_error(v)
        if isinstance(value, ErrorDetail):
            raise ValidationError(value)

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        自定义渲染，标准化返回值
        """
        response = renderer_context.get('response')
        _d = DataPackage(rc=response.status_code)
        if isinstance(data, dict):
            if 'fields' in data.keys():
                return super(Renderer, self).render(data, accepted_media_type, renderer_context)
            _d.set_fields(data.get('fields', data))
        elif isinstance(data, list):
            print('------')
            _d.set_elements(data)

        return super(Renderer, self).render(_d.dumps(), accepted_media_type, renderer_context)
