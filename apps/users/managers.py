from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Проверьте пожалуйста email'))

    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError(_("Придумайте никнейм"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Введите пожалуйста свой email'))
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff = TRUE")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser = TRUE")

        if extra_fields.get("is_active") is not True:
            raise ValueError("is_active = TRUE")

        if not username:
            raise ValueError(_("Придумайте никнейм"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Введите пожалуйста свой email'))
        user = self.create_user(username, email, password, **extra_fields)
        user.save(using=self._db)
        return user
