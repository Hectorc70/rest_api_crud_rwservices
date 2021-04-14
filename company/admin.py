from django.contrib import admin


from .models import (Company, Area, Activity, 
                    Picture, 
                    Task)
# Register your models here.
admin.site.register(Company)
admin.site.register(Area)
admin.site.register(Activity)
admin.site.register(Picture)
admin.site.register(Task)
