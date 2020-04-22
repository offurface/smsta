from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DocumentsConfig(AppConfig):
    """Default app config"""

    name = "apps.api.documents"
    verbose_name = _("Documents")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
