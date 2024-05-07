from django.http import HttpResponse
from django.shortcuts import render
from .models import UploadImage
from django.core.mail import send_mail
from django.http import JsonResponse

from .utils import load_trained_model, preprocess_image, predict_image_class

# Create your views here.

def homePage(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            uploaded_image = request.FILES['image']
            image_path = 'uploads/' + uploaded_image.name
            with open(image_path, 'wb') as f:
                for chunk in uploaded_image.chunks():
                    f.write(chunk)

            model_path = 'D:/LABS/AI/PDS Rep/Pneumonia-Detection-System/Website/PneumoniaDetectionSystem/CNN.h5' #path of the model
            loaded_model = load_trained_model(model_path)
            predicted_class, predictions = predict_image_class(loaded_model, image_path)

            # Interpret predictions as probabilities for each class
            probability_normal = predictions[0][0]  # Probability for Normal/Healthy class
            probability_pneumonia = predictions[0][1]  # Probability for Pneumonia class

            # Print the probabilities for each class
            print("Probability for Normal/Healthy class:", probability_normal)
            print("Probability for Pneumonia class:", probability_pneumonia)

            # Print the predicted class
            if predicted_class == 0:
                prediction_result = "You are normal."
                hasPneumonia = False
            else:
                prediction_result = "You have Pneumonia"
                hasPneumonia = True

            return render(request, 'result.html', {'prediction_result': prediction_result, 'hasPneumonia' : hasPneumonia})
        else:
            return HttpResponse('No image uploaded!')
    return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')


def about(request):
    return render(request, 'about.html')
    

def faqs(request):
    return render(request, 'faqs.html')
    
    
def privacy(request):
    return render(request, 'privacy.html')
    
    
def contact(request):
    return render(request, 'contact.html')
    
    
def terms(request):
    return render(request, 'terms.html')
    
    
def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Send email
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,  # Replace with your email address
            ['l215252@lhr.nu.edu.pk'],  # Replace with recipient email address
            fail_silently=False,
        )

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

    
    


