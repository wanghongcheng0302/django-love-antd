__doc__ = """编排代码
"""

from typing import List


class ComposerNode:

    def __init__(self, schema, component, relative_path):
        """
        编排的节点
        """
        self.schema = schema
        self.component = component
        self.relative_path = relative_path

        # 即使加载，及时生产代码
        self.compile()

    def compile(self):
        """
        编译代码
        """
        self.component(schema=self.schema).write(relative_path=self.relative_path)


class Composer:
    """
    借助dict，类似组合方式描述网站的图/布局

    字典描述布局和生成代码的顺序
    字典元素 = Component + Schema + 输出能力

    辅助的逻辑被拆散在Schema和mixins里了，模板只参与组件编排的功能，Composer作为调用方，统筹核心模块
    """

    def __init__(self):
        self.graph = dict()
