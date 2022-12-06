from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['username', 'email',
                    'is_staff', 'is_active', 'upper_get_full_name'
                    ]
    list_filter = ['username', 'email', 'is_staff', 'is_active']
    fieldsets = (
        (_("Авторизация"), {'fields': ('username', 'email', 'password')}),
        (_("Персональная информация"), {
            'fields': (
                'first_name', 'last_name'
            )}),
        (_("Разрешения"), {
            'fields': ('is_staff', 'is_active', 'is_superuser',)}),
        (_("Дополнительная информация"), {
            'fields': ('last_login', 'date_joined',)}),

    )
    add_fieldsets = (
        (None,
         {
             "classes": ("wide",),
             'fields': (
                 'username',
                 'email',
                 'password1',
                 'password2',
                 'is_staff',
                 'is_active'
             )
         }),
    )

    def upper_get_full_name(self, obj):
        return f'{obj.get_full_name()}'

    upper_get_full_name.short_description = 'ФИО'
