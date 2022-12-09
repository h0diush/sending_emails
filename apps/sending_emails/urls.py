from django.urls import path
from .views import HomePage, EmailCreateView, CreateGroupForEmailView

app_name = 'email'

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('create_email/', EmailCreateView.as_view(), name='create_email'),
    path('create_group/', CreateGroupForEmailView.as_view(),
         name='create_group'),
]
