import json

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpRequest
from main_app.generate_text import generate_text
from django.core.files.storage import FileSystemStorage
from main_app.embed_file import process_file, get_document

# Create your views here.
@csrf_exempt
@require_POST
def chat(request: HttpRequest):

    print("Session key:", request.session.session_key)

    summary = request.session.get("summary", "")
    print("previous summary", summary)

    data = json.loads(request.body)
    question = data["question"]
    context = get_document(data["question"])

    output = generate_text(
        f'''
        Question: {question},
        
        Context: {context}

        Previous conversation summary: {summary}

        If there is valid answer in the below context (also use the previous summary),
        then provide me that response.
        if the question not related to the above context then give your own response.
        '''
    )
    print("output: ", output)

    new_summary = generate_text("Generate some short summary for the text: " + output)
    print("New summary", new_summary)
    request.session["summary"] = new_summary

    print("Session key:", request.session.session_key)

    return JsonResponse({'answer': output})


@csrf_exempt
@require_POST
def upload_document(request):
    uploaded_file = request.FILES["file"]

    fs = FileSystemStorage(location="uploads/")
    filename = fs.save(uploaded_file.name, uploaded_file)
    process_file("uploads/"+filename)
    return HttpResponse("Success")
