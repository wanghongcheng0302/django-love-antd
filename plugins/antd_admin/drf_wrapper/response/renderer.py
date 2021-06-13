from rest_framework.renderers import JSONRenderer
from .response import DataPackage


class Renderer(JSONRenderer):
    def render(self, data, *args, **kwargs):
        _d = DataPackage()
        data_warp = dict()

        if isinstance(data, dict):
            if 'fields' in data.keys() or 'elements' in data.keys():
                return super(Renderer, self).render(data, *args, **kwargs)
            for k, v in data.items():
                if k == 'rc':
                    data_warp.update({'rc': v})
                    continue
                if k == 'error':
                    data_warp.update({'error': v})
                    continue
                _d.set_field(k, v)
                data_warp = _d.dumps()

        elif isinstance(data, list):
            _d.set_elements(data)
            data_warp = _d.dumps()
        return super(Renderer, self).render(data_warp, *args, **kwargs)
