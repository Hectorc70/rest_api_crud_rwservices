from django.urls import path
from .views import CompanyRecordView, AreaRecordView

app_name = 'company'
urlpatterns = [
    path('api-company/<company>', CompanyRecordView.as_view(), name='companys'),
    path('api-area/<company>', AreaRecordView.as_view(), name='areas'),
]