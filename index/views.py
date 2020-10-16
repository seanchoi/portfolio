from django.shortcuts import render, redirect
from login.models import Users, DMs

def index(request):
    user = Users.objects.get(user_id="comenseeme")
    dm = DMs.objects.filter(dm_to=user, if_check="no")
    logged_user=""
    if 'user_id' in request.session:
        logged_user = Users.objects.get(user_id=request.session['user_id'])
    return render(request, 'home.html', {'user':user, 'dm':dm, 'logged_user':logged_user})

def DM(request):
    if request.method == "POST":
        dm_to = Users.objects.get(user_id=request.POST['dm_to'])
        dm_from_name = request.POST['dm_from_name']
        dm_from_email = request.POST['dm_from_email']
        dm_msg = request.POST['dm_msg']
        DMs.objects.create(dm_to=dm_to, dm_from_name=dm_from_name, dm_from_email=dm_from_email, dm_content=dm_msg)
        return redirect('/')
    return redirect('/')

def checkDM(request):
    if 'user_id' not in request.session:
        return redirect('/')
    elif request.session['user_id'] == "comenseeme":
        dms = DMs.objects.filter(dm_to=Users.objects.get(user_id="comenseeme"))
        dms.update(if_check="yes")
        return render(request, 'dm.html', {'dms':dms})
    else:
        return redirect('/')

def deleteDM(request, dm_id):
    if request.session['user_id'] == "comenseeme":
        DMs.objects.get(id=dm_id).delete()
        return redirect('/dm_check/')
    return redirect('/')