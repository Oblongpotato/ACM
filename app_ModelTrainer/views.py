import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import ConfidentImage, NonConfidentImage
from django.views.decorators.csrf import csrf_exempt
import json


def TrainerInterface(request):
    # Get the list of images in the 'image_sample' folder located in the root directory
    image_folder = os.path.join(settings.BASE_DIR, 'image_sample')
    
    # Safeguard if the folder doesn't exist
    if not os.path.exists(image_folder):
        return render(request, 'app_ModelTrainer/TrainerInterface.html', {'images': []})

    # Collect image URLs
    image_files = os.listdir(image_folder)
    images = [{'url': f'/image_sample/{img}'} for img in image_files if img.lower().endswith(('png', 'jpg', 'jpeg'))]

    return render(request, 'app_ModelTrainer/TrainerInterface.html', {'images': images})


@csrf_exempt
def rate_image(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            image_name = data.get("image_name")
            confidence = data.get("confidence")

            if not image_name or not confidence:
                return JsonResponse({"status": "error", "message": "Invalid data provided."})

            image_path = f"media/sample_images/{image_name}"

            if confidence == "confident":
                ConfidentImage.objects.create(image_name=image_name, image_path=image_path)
            elif confidence == "not-confident":
                NonConfidentImage.objects.create(image_name=image_name, image_path=image_path)
            else:
                return JsonResponse({"status": "error", "message": "Invalid confidence value."})

            return JsonResponse({"status": "success", "message": f"Image {image_name} classified as {confidence}."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Error: {str(e)}"})
    return JsonResponse({"status": "error", "message": "Invalid request method."})