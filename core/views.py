#pylint:disable=E1101
from django.shortcuts import render, HttpResponse
from .models import Image
import random


def index(request):
	
	context={"home":"active text-primary"}
	
	return render(request, "index.html", context=context)



def background(request):
	
	imgs = list(Image.objects.all())
	random.shuffle(imgs)
	
	context={"background":"active text-primary", "imgs":imgs}
	
	return render(request, "background.html", context=context)



def logo(request):
	
	imgs = list(Image.objects.all())
	random.shuffle(imgs)
	
	context={"logo":"active text-primary", "imgs":imgs}
	
	return render(request, "logo.html", context=context)



def game(request):
	
	imgs = list(Image.objects.all())
	random.shuffle(imgs)
	
	context={"game":"active text-primary", "imgs":imgs}
	
	return render(request, "game.html", context=context)



def vfx(request):
	
	imgs = list(Image.objects.all())
	random.shuffle(imgs)
	
	context={"vfx":"active text-primary", "imgs":imgs}
	
	return render(request, "vfx.html", context=context)


def download_img(request, img_id):
	img_file = Image.objects.get(pk=img_id)
	imgName = f"Ap Assets - {img_file.img_name}"
	response = HttpResponse(img_file.img, content_type='application/force-download')
	response['Content-Disposition'] = f'attachment; filename="{imgName}"'
	return response