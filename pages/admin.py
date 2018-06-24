from django.contrib import admin
from pages.models import ClientCompany, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published',)
    list_filter = ('is_published',)


admin.site.register(ClientCompany)
admin.site.register(Feedback, FeedbackAdmin)
