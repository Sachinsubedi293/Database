from django.shortcuts import render
from .models import visit
def visit(request):
    context = {
        'visit':visit.objects.all()
    }
  
    return render(request,'hotel.html',context)


    