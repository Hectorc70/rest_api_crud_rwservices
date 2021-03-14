
from django.urls import path
from .views import (CompanyRecordView, 
                    AreaRecordView, 
                    ActivitysAreaRecordView,
                    ActivityRecordView,
                    PictureRecordView,
                    TaskRecordView)


app_name = 'company'
urlpatterns = [
    path('api-company/<company>', CompanyRecordView.as_view(), name='companys'),
    path('api-area/<company>', AreaRecordView.as_view(), name='areas'),
    path('api-activities-area/<area>', ActivitysAreaRecordView.as_view(), name='activities_area'),
    path('api-activity/<id_activity>', ActivityRecordView.as_view(), name='activity'),
    path('api-picture-activity/<id_activity>', PictureRecordView.as_view(), name='picture'),
    path('api-tasks-activity/<id_activity>', TaskRecordView.as_view(), name='task'),
] 