from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def error(request):
    return render(request, 'error.html')

def confirm_subscription(request):
    return render(request, 'confirm.html')

def plug_gig(request):
    return render(request, 'upload.html')