from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PhotoForm
from .models import Photo

result_url = {'Micro-USB-TypeB-2.0':'https://www.google.com/search?q=micro+usb+type-b+2.0+cable',
              'Micro-USB-TypeB-3.0':'https://www.google.com/search?q=micro+usb+type-b+3.0+cable',
              'Mini-USB-TypeB':'https://www.google.com/search?q=mini+usb+type-b', 
              'USB-TypeA':'https://www.google.com/search?q=USB+cable+type-A', 
              'USB-TypeC':'https://www.google.com/search?q=usb+type-c'}

def index(request):
    template=loader.get_template("usbai/index.html")
    form = PhotoForm()
    filename_save = '*現在ファイル名は表示されません'
    context={"form":form, "filename_save": filename_save}
    return HttpResponse(template.render(context,request))

def predict(request):
    if not request.method=="POST":
        return redirect("usbai:index")
    form=PhotoForm(request.POST,request.FILES)
    if not form.is_valid():
        raise ValueError("Formが不正です")

    photo=Photo(image=form.cleaned_data["image"])
    predicted,percentage=photo.predict()

    template=loader.get_template("usbai/result.html")

    context={
        "photo_name":photo.image.name,
        "photo_data":photo.image_src(),
        "predicted":predicted,
        "percentage":percentage,
        "result_url":result_url[predicted],
    }
    return HttpResponse(template.render(context,request))


