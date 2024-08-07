from django.http import HttpResponse


def home_page(request):
    print("homepage")
    return HttpResponse("This is homepage")
