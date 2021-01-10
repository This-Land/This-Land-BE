from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect("https://this-land-team-5.herokuapp.com/admin/")

    