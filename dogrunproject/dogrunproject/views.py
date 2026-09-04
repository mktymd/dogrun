from django.shortcuts import render

def index(request):
    return render(request, "dogruns/index.html")

def mypage(request):
    return render(request, "dogruns/mypage.html")
# comment