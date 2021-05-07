from django.shortcuts import render
from home.models import Setting, Images
# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    photo = Images.objects.all().order_by('-id')
    context = {'setting': setting,
               'photo': photo,
              }
    return render(request, 'index.html', context)