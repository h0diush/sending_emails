from django.urls import path
from .views import HomePage, EmailCreateView, CreateGroupForEmailView, \
    SendMessageEmailView, EmailDeleteView

app_name = 'email'

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('create_email/', EmailCreateView.as_view(), name='create_email'),
    path('create_group/', CreateGroupForEmailView.as_view(),
         name='create_group'),
    path('email/<int:pk>/', SendMessageEmailView.as_view(),
         name='detail_email'),
    path('email/<int:pk>/delete/', EmailDeleteView.as_view(),
         name='delete_email'),
]
