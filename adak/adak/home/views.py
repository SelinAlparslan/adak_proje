from django.shortcuts import render
from home.models import Setting, Images, ContactFormMessage, ContactFormu
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

def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, "Mesajınız başarılı bir şekilde gönderilmiştir.")
            return HttpResponseRedirect('')
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting,
               'form': form,
              }
    return render(request, 'contact.html', context)

def photo_detail(request, id):
    setting = Setting.objects.get(pk=1)
    photo = Images.objects.get(pk=id)
    context = {'setting': setting,
                'photo': photo}
    return render(request, 'photo_detail.html', context)
