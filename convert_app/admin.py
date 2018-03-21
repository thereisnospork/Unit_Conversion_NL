from django.contrib import admin

from .models import unitOfMeasure, prefix

admin.site.register(unitOfMeasure)
admin.site.register(prefix)
