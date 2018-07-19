from django.contrib import admin
from pages.models import ClientCompany, Feedback, Document, Faq

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published',)
    list_filter = ('is_published',)


admin.site.register(ClientCompany)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Document)
admin.site.register(Faq)
