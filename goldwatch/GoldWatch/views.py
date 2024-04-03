from django.shortcuts import render
from . models import GoldCard
# Create your views here.

def index(request):
    records = GoldCard.objects.all()
    return render(request,'index.html',{'records':records})