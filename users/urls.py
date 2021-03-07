from django.urls import path
from .views import UserRecordView

app_name = 'users'
urlpatterns = [
    path('user/<user_id>', UserRecordView.as_view(), name='users'),
]