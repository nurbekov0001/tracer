from django.contrib import admin
from webapp.models import Tracer, Status, Type


class TracersAdmin(admin.ModelAdmin):
    list_display = ['id', 'surname', 'description', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    fields = ['surname', 'description', 'status']


admin.site.register(Tracer, TracersAdmin)
admin.site.register(Type)
admin.site.register(Status)
# Register your models here.
