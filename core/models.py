from django.db import models


class Image(models.Model):
	
	TYPE_CHOICES = (
    ("BACKGROUND", "background"),
    ("LOGO", "logo"),
    ("GAME", "game"),
    ("VFX", "vfx"),
)

	img_type = models.CharField(max_length=10,
                  choices=TYPE_CHOICES,
                  default="BACKGROUND")
                  
	img_name = models.CharField(max_length=100, default="Image from Ap Assets")
	img = models.FileField(upload_to="img/")