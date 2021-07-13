__doc__ = """jinja2过滤器
"""


def namespace_to_blueprint(namespace):
    if not namespace:
        return
    return '/'.join(namespace.split('.'))
