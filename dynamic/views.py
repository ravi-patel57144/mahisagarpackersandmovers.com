from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from dynamic.models import Pages, Quote, Branch


# Create your views here.

def branch(request):
    branch = Branch.objects.all()
    return render(request, 'home/branches.html', context={'branches': branch})

def city_pages(request, city):
    page = get_object_or_404(Pages, city=city)
    return render(request, 'dynamic/city_pages.html', context={ 'city_pages': page })

def quotation(request):
    if request.method == 'POST':
        try:
            Quote.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                mobile=request.POST.get('mobile'),
                date=request.POST.get('date'),
                s_from=request.POST.get('s_from'),
                s_to=request.POST.get('s_to'),
                message=request.POST.get('message')
            )
        except:
            return HttpResponse("ERROR WHILE SUBMITTING DATA")
        return render(request, 'home/index.html', context={'msg': 'success'})