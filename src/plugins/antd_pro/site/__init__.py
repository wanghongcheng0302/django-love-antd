__doc__ = '''管理后台
'''

from antd_pro.core.composers import Composer, ComposerNode
from antd_pro.site.mycode.backend.src.api.serializers import Serializer
from antd_pro.site.mycode.backend.src.api.viewsets import ViewSet
from antd_pro.site.mycode.backend.src.api.urls import Url
from antd_pro.core.schemas import Schema
from antd_pro.core.components import CopyComponent
import os

composer = Composer()

schemas = Schema.schemas

# 后端接口
composer.graph = {'backend': {'src': {'serializers': None, 'viewsets': None, 'urls': None, 'common': None}}}

composer.graph['backend']['src']['serializers'] = ComposerNode(
    schema=schemas,
    component=Serializer,
    relative_path=os.path.join('backend', 'src', 'api', 'serializers.py'),
)

composer.graph['backend']['src']['viewsets'] = ComposerNode(
    schema=schemas,
    component=ViewSet,
    relative_path=os.path.join('backend', 'src', 'api', 'viewsets.py'),
)

composer.graph['backend']['src']['urls'] = ComposerNode(
    schema=schemas,
    component=Url,
    relative_path=os.path.join('backend', 'src', 'api', 'urls.py'),
)

# 公共代码

