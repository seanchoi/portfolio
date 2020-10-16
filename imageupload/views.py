from django.shortcuts import render, redirect
from .forms import *
from .models import *
from imageupload.models import *
from django.http import JsonResponse

def multipleImg(request):
    imgs = Images.objects.all()
    memos = Memos.objects.all()
    return render(request, 'multiple.html',{'imgs':imgs,'memos':memos})

def imageUpload(request):
    form = PhotoForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.save()        
        data = {'is_valid': True, 'name': image.files.name, 'url': image.files.url}
    else:
        data = {'is_valid': False}
    return JsonResponse(data)

def clear_images(request):
    for photo in Images.objects.all():
        photo.files.delete()
        photo.delete()
    return redirect(f'/multiple_img')

def newMemo(request):
    if request.method == "POST":
        subject = request.POST['subject']
        content = request.POST['content']
        images = Images.objects.all()
        imgs = [''] * 4        
        for i in range(len(imgs)):
            if len(images) > i:
                imgs[i] = images[i].files
        Memos.objects.create(subject=subject, content=content, img01=imgs[0], img02=imgs[1], img03=imgs[2], img04=imgs[3])        
        Images.objects.all().delete() 
        return redirect('/multi/multiple_img/')
    return redirect('/multi/multiple_img/')

def deleteMemo(request, memo_id):    
    Memos.objects.get(id=memo_id).delete()
    return redirect('/multi/multiple_img/')