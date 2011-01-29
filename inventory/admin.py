from django.contrib import admin
from pantry.inventory import models

#class AuthorAdmin(admin.ModelAdmin):
 #       pass
admin.site.register(models.Food)
admin.site.register(models.Category)
admin.site.register(models.Purchase)
admin.site.register(models.MeasurementUnit)
admin.site.register(models.Store)
admin.site.register(models.Brand)
