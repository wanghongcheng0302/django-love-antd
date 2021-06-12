from . import BaseParser
from .app import AppParser
from typing import Optional, List


class SiteParser(BaseParser):

    @property
    def apps(self):
        return self.get_apps()

    @property
    def title(self):
        return self.get_title()

    @property
    def copyright(self):
        return self.get_copyright()

    @property
    def icon(self):
        return self.get_icon()

    def get_title(self) -> str:
        pass

    def get_copyright(self) -> str:
        pass

    def get_icon(self) -> str:
        pass

    def get_apps(self) -> Optional[List[AppParser]]:
        pass
