from django.contrib import admin
from .models import Project, Tag
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display= ('title', 'priority')

admin.site.register(Project,ProjectAdmin)
admin.site.register(Tag)
