from django.shortcuts import render, HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
def index(request):
    if request.method == 'POST':
        # print(request.POST, request.body)
        i1 = int(request.POST.get("i1"))
        i2 = int(request.POST.get("i2"))
        return HttpResponse(i1+i2)

        # print("test", i1, i2, type(i1), i1)
    return render(request, 'index1.html')


@ensure_csrf_cookie
def ajax_test(request):
    if request.method == 'POST':
        hobby = json.loads(request.POST.get("hobby"))
        name = request.POST.get("name")
        print(hobby, name)
        data = {'key': 'value',
                'key_list': [1, 2, 3, 4]
                }
        return JsonResponse(data)
    return render(request, 'ajaz.html')