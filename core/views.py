from django.http import HttpResponseRedirect

def index_page(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/admin")


# Create your views here.
# def index_page(request):
#     return render(request, "core/index_page.html")
    