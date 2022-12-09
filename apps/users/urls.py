from django.contrib.auth import views as auth_views
from django.urls import path
from registration.backends.default.views import (ActivationView,
                                                 ResendActivationView)

from .views import (ActivationEmailComplete, LoginUserView, logout_user,
                    PasswordChange, PasswordResetView, RegistrationUserView)

urlpatterns = [
    path('register/', RegistrationUserView.as_view(), name='register'),
    path(
        'login/',
        LoginUserView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('logout/', logout_user, name='logout'),
    # path('update/', UpdateUserView.as_view(), name='update'),
    # path('delete/', DeleteUserView.as_view(), name='delete'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password-reset/', PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('activate/complete/',
         ActivationEmailComplete.as_view(),
         name='registration_activation_complete'),
    path('activate/resend/',
         ResendActivationView.as_view(),
         name='registration_resend_activation'),
    path('activate/<activation_key>/',
         ActivationView.as_view(),
         name='registration_activate'),
]
