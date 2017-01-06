from django.contrib import admin
from scms.content.models import *


class ContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Content, ContentAdmin)
