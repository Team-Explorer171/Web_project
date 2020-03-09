from django.shortcuts import render, redirect
from .models import ScrapbookTable


# Create your views here.
def index(request):
    if request.method == 'POST':
        photo = request.POST.get('image_up')
        title = request.POST.get('title_input')
        experiences = request.POST.get('ex_input')
        scrap = ScrapbookTable(picture=photo, title=title, experience=experiences)
        scrap.save()
        return redirect('/')
    details = ScrapbookTable.objects.all()
    return render(request, 'html/index.html', {"context": details})


# def home(request):
#
#     return render(request, 'html/index.html', context)
