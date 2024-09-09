from django.contrib import admin
from .models import *



@admin.register(DocumentModel)
class DocumentModelAdmin(admin.ModelAdmin):
    pass