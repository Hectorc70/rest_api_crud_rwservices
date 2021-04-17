
from django.urls import path, include
from .views import (CompanyRecordView, 
                    AreaRecordView, 
                    ActivitysAreaRecordView,
                    ActivityRecordView,
                    ActivitysUserRecordView
                    PictureRecordView,
                    TaskRecordView)


app_name = 'company'
urlpatterns = [
    path('api-company/<company>', CompanyRecordView.as_view(), name='companys'),
    
    path('api-area/<company>', AreaRecordView.as_view(), name='areas'),
    
    path('api-activities-area/<area>', ActivitysAreaRecordView.as_view(), name='activities_area'),
    path('api-activities-user/<id_user>', ActivitysUserRecordView.as_view(), name='activities_user'),
    path('api-activity/<id_activity>', ActivityRecordView.as_view(), name='activity'),
    path('api-activity/', ActivityRecordView.as_view(), name='activity'),
    
    path('api-picture/', PictureRecordView.as_view(), name='picture'),
    path('api-pictures-activity/<id_activity>', PictureRecordView.as_view(), name='picture'),

    
    path('api-task/', TaskRecordView.as_view(), name='task'),
    path('api-tasks-activity/<id_activity>', TaskRecordView.as_view(), name='task'),
    
] 