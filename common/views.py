from django.shortcuts import render

from django.views import View
from django.http import HttpRequest, HttpResponse

class HelloWorldView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        hello = """<h1>Hello, World</h1>"""
        return HttpResponse(hello)

class IndexView(View):
    def get(self, request):
        return render(request, "common/index.html")