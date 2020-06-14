from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)
from rest_framework_simplejwt.token_blacklist.admin import (
    OutstandingTokenAdmin,
    BlacklistedTokenAdmin,
)

from apps.core.utils.admin import BaseAdminMixin

from .models import (
    ProxyGroup,
    User,
    ProxyBlacklistedToken,
    ProxyOutstandingToken,
)


@admin.register(User)
class UserAdmin(BaseAdminMixin, BaseUserAdmin):
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "last_name",
                    "first_name",
                    "patronymic",
                    "email",
                    "employe_position",
                    "phone",
                    "role",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.unregister(BaseGroup)
admin.site.unregister(OutstandingToken)
admin.site.unregister(BlacklistedToken)

admin.site.register(ProxyGroup, GroupAdmin)
admin.site.register(ProxyOutstandingToken, OutstandingTokenAdmin)
admin.site.register(ProxyBlacklistedToken, BlacklistedTokenAdmin)
