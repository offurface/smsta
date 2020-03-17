from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup
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


admin.site.unregister(BaseGroup)
admin.site.unregister(OutstandingToken)
admin.site.unregister(BlacklistedToken)

admin.site.register(ProxyGroup, GroupAdmin)
admin.site.register(ProxyOutstandingToken, OutstandingTokenAdmin)
admin.site.register(ProxyBlacklistedToken, BlacklistedTokenAdmin)
