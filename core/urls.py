
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("background/", views.background, name="background"),
    path("logo/", views.logo, name="logo"),
    path("game/", views.game, name="game"),
    path("vfx/", views.vfx, name="vfx"),
    path("Download/<int:img_id>", views.download_img, name="download_img"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
