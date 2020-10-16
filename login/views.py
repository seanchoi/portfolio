import bcrypt
import re
from django.shortcuts import render, redirect
from login.models import Users
from django.contrib import messages

# REGISTRATION PAGE
# registration form validation by ajax
# email check with re (REGEX)
# password encode by bcrypt

def nameCheck(request, name):
    found = ""
    data = request.POST[f'{name}']    
    if len(data) == 0:
        found = "required"
    if len(data) > 0 and len(data) < 2:
        found = "short"
        if not data[0].isalpha():
            found = "special"      
        # for i in range(len(data)):
        #     if not data[i].isalpha():
        #         found = True
    else:
        for i in range(len(data)):
            if not data[i].isalpha():
                found = "special"
            else:
                found = False         
    context = {
        'found' : found
    }
    return render(request, 'partials/name.html', context)

def emailCheck(request):
    found = False
    data = request.POST['email']
    if len(data) == 0:
        found = "required"    
    if len(data)>0:
        found="nothing"        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data):
            found = "not valid"
        else:
            users = Users.objects.filter(email=data)    
            if len(users):
                found = "duplicate"
            else:
                found=False
    context = {
        'found' : found,
    }
    return render(request, 'partials/email.html', context)

def userIdCheck(request):
    data = request.POST['user_id']
    users = Users.objects.filter(user_id=data)    
    found = ""
    if len(data) == 0:
        found = "required"
    if len(data) > 0 and len(data) < 6:
        found = "short"
    elif len(data) > 5:
        found = False
        if len(users):
            found = True
        else:
            found = False
    context = {
        'found' : found
    }
    return render(request, 'partials/user_id.html', context)

def passwordCheck(request):
    data = request.POST['password']
    found = ""
    if len(data) == 0:
        found = "required"
    if len(data) > 0 and len(data)< 6:
        found = "short"
    elif len(data) > 6:
        found = False
    context = {
        'found' : found
    }
    return render(request, 'partials/pass.html', context)

# registration
def register(request):
    if request.method == "POST":
        errors = Users.objects.validator(request.POST)
        if len(errors):
            for key, val in errors.items():
                messages.error(request, val)
                return redirect('/register')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user_id = request.POST['user_id'].lower()
            email = request.POST['email']
            password = request.POST['password']            
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = Users.objects.create(first_name=first_name, last_name=last_name, user_id=user_id, email=email, password=pw_hash)                      
            return redirect('/register/')
    return render(request, 'register.html')

# LOGIN PAGE
def loginIdCheck(request):
    data = request.POST['user_id']
    users = Users.objects.filter(user_id=data)
    found = ""
    if len(data) == 0:
        found = "required"
    if len(data) >0 and len(data)<6:
        found = "not exist"
    if len(data) > 5:    
        if users:
            found = True
        else:
            found = "not found"
    context = {
        'found' : found
    }
    return render(request, 'partials/login_id.html', context)

def login(request):
    if request.method == "POST":
        user = Users.objects.filter(user_id=request.POST['user_id'])
        if len(user):
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.user_id
                return redirect(f'/{user[0].user_id}/')
    return render(request, 'register.html')

def dashboard(request, user_id):
    user = Users.objects.filter(user_id=user_id)
    if not user:
        return redirect('/register/')
    else:
        return render(request, 'dashboard.html', {'user':user[0]})

def profilePic(request, user_id):
    if request.method == "POST":        
        user = Users.objects.get(user_id=user_id)                  
        profile_pic = ""
        if request.FILES.get('profile_pic'):
            user.profile_pic.delete() 
            profile_pic =  request.FILES.get('profile_pic')
            user.profile_pic = profile_pic
            user.save()
        return redirect(f'/{user_id}/')
    else:
        if 'user_id' not in request.session:
            return redirect('/')
        return redirect(f'/{user_id}/')

def profilePicDelete(request, user_id):
    if 'user_id' not in request.session:
        return redirect(f'/{user_id}/')
    elif user_id != request.session['user_id']:
        return redirect(f'/{user_id}/')
    else:
        user = Users.objects.get(user_id=user_id)
        user.profile_pic.delete()
        return redirect(f'/{user_id}/')

def logout(request):
    request.session.flush()
    return redirect('/register/')

