from django.shortcuts import redirect, HttpResponse


# class Ret(object):
#     def __init__(self, req):
#         self.req = req
#
#     def render(self):
#         return HttpResponse("rend")


# Create your views here.
def test(request):
    print("app01 中的 test")

    def render():
        print("in test/render")
        return HttpResponse("O98K")
    rep = HttpResponse("OK")
    rep.render = render
    return rep

