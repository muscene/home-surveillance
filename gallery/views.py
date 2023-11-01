from django.shortcuts import render
from .models import Image
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
import cv2
from django.http import StreamingHttpResponse
import time
import os
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# def image_list(request):
#     images = Image.objects.all()
#     return render(request, 'image_list.html', {'images': images})
def image_list(request):
    images = Image.objects.all()
    return render(request, 'image.html', {'images': images})
def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload.html', {'form': form})
def image_delete(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery:image_list')
    return render(request, 'image_delete.html', {'image': image})