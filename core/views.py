from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    return render(request, "pages/home.html")




# Create your views here.
# def index_page(request):
#     return render(request, "core/index_page.html")
    