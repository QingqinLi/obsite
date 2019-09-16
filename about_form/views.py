from django.shortcuts import render, HttpResponse
from about_form.forms import *


# Create your views here.
def register(request):
    form_obj = RegForm()
    if request.method == 'POST':

        form_obj = RegForm(request.POST)
        print(request.body)
        if form_obj.is_valid():
            print(form_obj.cleaned_data)
            return HttpResponse("注册成功")
    return render(request, "register.html", {"form_obj": form_obj})