from django.contrib import admin
from . import models

admin.site.register(models.UrlItem)
admin.site.register(models.RequestItem)

