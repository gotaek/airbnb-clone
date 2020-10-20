from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Review)
class ReviewAdmiin(admin.ModelAdmin):
    """ Review Admin Definition """

    pass

    list_display = ("__str__", "rating_average")
