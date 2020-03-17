from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SystemConfig(AppConfig):
    """Default app config"""

    name = "apps.api.system"
    verbose_name = _("System")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
