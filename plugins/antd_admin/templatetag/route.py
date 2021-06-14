from . import BaseTemplateTag
import os


class RouteTemplateTag(BaseTemplateTag):
    routes_tpl = os.path.join('frontend', 'config', 'routes.tpl')
    app_routes_tpl = os.path.join('frontend', 'config', 'app_routes.tpl')
    model_routes_tpl = os.path.join('frontend', 'config', 'model_routes.tpl')

    def write(self):
        content = self.get_routes(self.data['apps'])
        with open('tmp.ts', 'w') as f:
            f.write(content)

    def get_app_routes(self, app):
        template = self.render.env.get_template(self.app_routes_tpl)
        model_routes = [self.get_model_routes(model_config) for model_name, model_config in app['models'].items()]

        content = template.render(model_routes=model_routes, app=app)
        return content

    def get_model_routes(self, model):
        template = self.render.env.get_template(self.model_routes_tpl)

        content = template.render(model=model)
        return content

    def get_routes(self, apps):
        template = self.render.env.get_template(self.routes_tpl)

        app_routes = [self.get_app_routes(app_config) for app_name, app_config in apps.items()]

        content = template.render(app_routes=app_routes, site=apps)
        return content
