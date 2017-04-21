from django.contrib import admin
from blog.models import Blog, Category, MailBox
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    exclude = ['']

class MailBoxAdmin(admin.ModelAdmin):
    exclude= ['myEmails','connected']

admin.site.register(Blog, BlogAdmin)
admin.site.register(MailBox, MailBoxAdmin)
