from django.urls import path
from .views import CompanyRecordView

app_name = 'company'
urlpatterns = [
    path('api-company/', CompanyRecordView.as_view(), name='companys'),
]