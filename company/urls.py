from django.urls import path
from .views import (CompanyRecordView, 
                    AreaRecordView, 
                    ActivitysAreaRecordView,
                    ActivityRecordView)

app_name = 'company'
urlpatterns = [
    path('api-company/<company>', CompanyRecordView.as_view(), name='companys'),
    path('api-area/<company>', AreaRecordView.as_view(), name='areas'),
    path('api-activitys-area/<area>', ActivitysAreaRecordView.as_view(), name='activities_area'),
    path('api-activity/<id_activity>', ActivityRecordView.as_view(), name='activitie'),
]