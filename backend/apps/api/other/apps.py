from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OtherConfig(AppConfig):
    """Default app config"""

    name = "apps.api.other"
    verbose_name = _("Other")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
