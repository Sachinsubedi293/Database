from django.shortcuts import render
from .models import pictures
def pictures(request):
    context = {
        'pictures':pictures.objects.all()
    }
  
    return render(request,'hotel.html',context)


    