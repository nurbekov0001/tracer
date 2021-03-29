from django.contrib import admin
from webapp.models import Tracer, Status, Type, Project


class TracersAdmin(admin.ModelAdmin):
    list_display = ['id', 'surname', 'description', 'status', 'created_at', 'updated_at', 'project']
    list_filter = ['status']
    fields = ['surname', 'description', 'status', 'project']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'start_data', 'end_data']
    list_filter = ['name']
    fields = ['name', 'description']


admin.site.register(Tracer, TracersAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project, ProjectAdmin)
# Register your models here.
