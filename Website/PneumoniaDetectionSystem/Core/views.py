from django.http import HttpResponse
from django.shortcuts import render
from .models import UploadImage
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

            model_path = 'F:/Website/Website/PneumoniaDetectionSystem/CNN.h5' #path of the model
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
            else:
                prediction_result = "You have Pneumonia"

            return render(request, 'result.html', {'prediction_result': prediction_result})
        else:
            return HttpResponse('No image uploaded!')
    return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')


