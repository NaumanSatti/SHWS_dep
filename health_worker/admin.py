from pyexpat import model
from django.contrib import admin
from .models import HealthWorker, District, Report
from django.contrib.auth.models import User

# class UserAdmin(admin.TabularInline):
#     model = User
class HealthWorkerAdmin(admin.ModelAdmin):
    model = HealthWorker
    list_filter = ["user","district"]


    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Image Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(HealthWorker, HealthWorkerAdmin)
admin.site.register(District)
admin.site.register(Report)
# Register your models here.
