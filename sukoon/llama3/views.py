from django.shortcuts import render
from .utils import model_id,pipeline
from django.http import JsonResponse

def respond(request):
    if request=="POST":
        user_input = request.POST.get('text')
        results = pipeline(user_input)
        return JsonResponse(results, safe=False)
    return render(request, 'llama3/respond.html')
