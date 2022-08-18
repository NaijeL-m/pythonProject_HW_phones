from django.contrib import admin
from .models import Phones

@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    pass
# Register your models here.
