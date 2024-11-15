from django.shortcuts import render, redirect
from .models import ChatMessage
from django.views.decorators.csrf import csrf_exempt
import predict_confidence
# from django.http import HttpResponse


@csrf_exempt
def chat(request):
    if request.method == 'POST':
        image = request.FILES.get('image')  # Get the uploaded image
        caption = request.POST.get('caption', '')  # Get the caption if provided
        
        # Set default caption to the image filename if no caption is provided
        if image:
            if not caption and image:
                caption = image.name
            # system_response = "This is a default response." + caption
        
            # Predict confidence based on the uploaded image
            confidence_label = predict_confidence.predict_confidence(image)
            system_response = f"The system predicts the person in '{caption}' is {confidence_label}. "
            
            # Save both user message and system response to the database
            chat_message = ChatMessage(user_image=image, caption=caption, system_response=system_response)
            chat_message.save()
        
        else:
            # Handle case where no image is uploaded
            return render(request, 'app_Chats/chat.html', {
                'chat_history': ChatMessage.objects.all().order_by('timestamp'),
                'error': 'Please upload an image to proceed.'
            })
        
    # Retrieve all chat messages from the database to display as chat history
    chat_history = ChatMessage.objects.all().order_by('timestamp')
    return render(request, 'app_Chats/chat.html', {'chat_history': chat_history})


def clear_chat(request):
    if request.method == 'POST':
        ChatMessage.objects.all().delete()
        return redirect('chat')
    else:
        return redirect('chat')