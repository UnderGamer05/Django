from django.contrib import admin
from .models import Image



@admin.register(Image)
class ImageReg(admin.ModelAdmin):
	list_display = ("id", "img_name", "img_type", "img")

