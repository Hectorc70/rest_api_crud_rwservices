from django.urls import path
from .views import CompanyRecordView, AreaRecordView, ActivityRecordView

app_name = 'company'
urlpatterns = [
    path('api-company/<company>', CompanyRecordView.as_view(), name='companys'),
    path('api-area/<company>', AreaRecordView.as_view(), name='areas'),
    path('api-activity/<area>', ActivityRecordView.as_view(), name='activities'),
]