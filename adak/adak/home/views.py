from django.shortcuts import render
from home.models import Setting, Images
# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    photo = Images.objects.all().order_by('?')
    randomphoto = Images.objects.all().order_by('-id')[:9]
    context = {'setting': setting,
               'photo': photo,
               'randomphoto': randomphoto,
              }
    return render(request, 'index.html', context)


def photo_detail(request, id):
    setting = Setting.objects.get(pk=1)
    photo = Images.objects.get(pk=id)
    context = {'setting': setting,
                'photo': photo}
    return render(request, 'photo_detail.html', context)
