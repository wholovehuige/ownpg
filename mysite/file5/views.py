from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import os

# Create your views here.
FILE_PATH = "C:\\Users\\soabs\\data_home\\git_data\\ownpg\\mysite\\file5\\upload\\"


class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            f_path = os.path.join(FILE_PATH, username)
            if os.path.exists(f_path) == False:
                os.makedirs(f_path)
            f_path = os.path.join(f_path,headImg.name)
            f = open(f_path, 'wb')
            try:
                for item in headImg.chunks(chunk_size=1024):
                    f.write(item)
                user = User()
                user.username = username
                user.headImg = FILE_PATH + username
                user.save()
            except Exception as e:
                print(e.__str__())
            finally:
                f.close()
            users = User.objects.all()
            return render(request, "file/fileupload.html", {"users": users})
    else:
        uf = UserForm
    return render_to_response('file/register.html', {'uf': uf})

def users(request):
    users  = User.objects.all()
    return render(request,"file/fileupload.html",{"users":users})

