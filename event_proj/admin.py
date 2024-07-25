from django.contrib import admin
from .models import Events, Role, Department
# Register your models here.
admin.site.register(Events)
admin.site.register(Role)
admin.site.register(Department)
