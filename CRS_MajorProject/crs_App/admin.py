from django.contrib import admin
from crs_App.models import *

# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

admin.site.register(EducationModel,EducationAdmin)

class HealthAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

admin.site.register(HealthModel,HealthAdmin)

class AgricultureAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

admin.site.register(AgricultureModel,AgricultureAdmin)

class ElectricityAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

admin.site.register(ElectricityModel,ElectricityAdmin)

class BusinessAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

admin.site.register(BusinessModel,BusinessAdmin)

class YouthAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

admin.site.register(YouthModel,YouthAdmin)

class GovJobsAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

admin.site.register(GovernmentJobsModel,GovJobsAdmin)

