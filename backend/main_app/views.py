import json

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from main_app.generate_text import generate_text
from django.core.files.storage import FileSystemStorage
from main_app.embed_file import process_file

# Create your views here.
@csrf_exempt
@require_POST
def chat(request):
    data = json.loads(request.body)
    output = generate_text(data["question"])
    return JsonResponse({'answer': output})


@csrf_exempt
@require_POST
def upload_document(request):
    uploaded_file = request.FILES["file"]

    fs = FileSystemStorage(location="uploads/")
    filename = fs.save(uploaded_file.name, uploaded_file)
    process_file("uploads/"+filename)
    return HttpResponse("Success")
