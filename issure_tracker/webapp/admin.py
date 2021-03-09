from django.contrib import admin
from webapp.models import Tracer, Status, Type


class TracersAdmin(admin.ModelAdmin):
    list_display = ['id', 'surname', 'description', 'status', 'type']
    list_filter = ['status', 'type']
    fields = ['surname', 'description', 'status', 'type']


admin.site.register(Tracer, TracersAdmin)
admin.site.register(Type)
admin.site.register(Status)
# Register your models here.
