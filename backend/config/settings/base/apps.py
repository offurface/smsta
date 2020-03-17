DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "import_export",
    "corsheaders",
    "widget_tweaks",
    "rest_framework",
    "drf_yasg",
    "django_cleanup.apps.CleanupConfig",
    "webpack_loader",
    "constance",
    "constance.backends.database",
    "etc",
    "drf_multiple_model",
    "rest_framework_simplejwt.token_blacklist",
]

PROJECT_APPS = [
    "apps.core.utils",
    "apps.core.main",
    "apps.core.api",
    "apps.api.auth",
    "apps.api.other",
    "apps.api.system",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]
