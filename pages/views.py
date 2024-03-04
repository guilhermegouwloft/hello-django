from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<html><title>Django</title><body>Hello, Django!</body></html>')