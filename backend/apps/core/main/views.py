from django.views.generic.base import TemplateView


class AppView(TemplateView):
    """Application view"""

    template_name = "app.html"
