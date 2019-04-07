from django.contrib import admin
from .models import Camp, CampComment, CampDates, CampPhoto


class CampPhotoInline(admin.TabularInline):
    model = CampPhoto
    extra = 0


class CampDatesInline(admin.TabularInline):
    model = CampDates
    extra = 0


class CampAdmin(admin.ModelAdmin):
    inlines = (CampDatesInline, CampPhotoInline,)
    list_display = ('__str__', 'slug')


admin.site.register(Camp, CampAdmin)
admin.site.register(CampComment)
